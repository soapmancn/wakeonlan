from flask import Flask, request, jsonify
import socket
import binascii
import logging
from datetime import datetime

app = Flask(__name__)

# 设置日志记录器
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')


@app.before_request
def log_request_info():
    # 获取请求的IP地址
    client_ip = request.remote_addr
    # 获取当前时间
    request_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # 记录日志
    logging.info(f"Request received from {client_ip} at {request_time}")
    

def send_wol_magic_packet(mac_address, broadcast_ip="255.255.255.255", port=9):
    mac_bytes = binascii.unhexlify(mac_address.replace(":", "").replace("-", ""))
    magic_packet = b'\xFF' * 6 + mac_bytes * 16

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        s.sendto(magic_packet, (broadcast_ip, port))


@app.route('/wol', methods=['POST'])
def wake_on_lan():
    data = request.get_json()

    target_mac_address = data.get('mac_address')

    if not target_mac_address:
        return jsonify({'error': 'MAC地址未提供'}), 400

    send_wol_magic_packet(target_mac_address)
    return jsonify({'message': 'Wake-on-LAN信号已发送'})


if __name__ == '__main__':
    app.run()
