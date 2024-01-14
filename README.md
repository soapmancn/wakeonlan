# wakeonlan
局域网唤醒开机

在局域网docker内搭建一个唤醒开机的api接口

使用以下方式调用： curl -X POST -H "Content-Type: application/json" -d '{"mac_address": "00:11:22:33:44:55"}' http://127.0.0.1:5000/wol

# github actions
需要添加docker hub的token，Settings--Security--Actions--Repository secrets
DOCKERHUB_TOKEN dockerhub生成的token
DOCKERHUB_USERNAME dockerhub用户名
