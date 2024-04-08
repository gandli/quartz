---
title: VPS禁用用户名密码登录，启用 SSH 登录
draft: false
tags:
  - VPS
  - SSH
  - 安全
  - jq
  - Docker
  - curl
  - Debian
  - apt
---

1. 本地
 首先，在本地生成 SSH 公钥，并将其复制到 VPS 上：

 ```bash
 ssh-keygen -y -f ~/.ssh/private_key > ~/.ssh/private_key.pub
 ssh-copy-id username@your_vps_ip
 ```

2. VPS
 登录到您的 VPS 后，执行以下命令修改 SSH 配置，以启用 SSH 密钥认证并禁用密码登录：

 ```bash
 sudo sed -i 's/#PubkeyAuthentication yes/PubkeyAuthentication yes/' /etc/ssh/sshd_config
 sudo sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config
 sudo sed -i 's/#ChallengeResponseAuthentication yes/ChallengeResponseAuthentication no/' /etc/ssh/sshd_config
 sudo sed -i 's/UsePAM yes/UsePAM no/' /etc/ssh/sshd_config
 sudo systemctl restart sshd
 ```

## 安装`jq`

`jq` 是一个强大的 JSON 处理工具。可以通过以下命令安装：

```bash
wget -O /usr/bin/jq https://github.com/jqlang/jq/releases/download/jq-1.7.1/jq-linux-amd64 && chmod +x /usr/bin/jq
jq --version
```

## 安装curl

`curl` 是一个常用的命令行工具，用于发送请求。安装方法如下：

```bash
apt update -y && apt install curl -y
curl --version
```

## 脚本安装 Docker

Docker 是一个开放平台，用于开发、交付和运行应用。通过以下脚本快速安装 Docker：

```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh ./get-docker.sh
docker -v
```  

## 禁用 `root` ，创建 `user`

```bash
useradd -m user && echo "user:password" | chpasswd
usermod -aG sudo user
sed -i 's/#PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config || sed -i 's/PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config
systemctl restart sshd
```
