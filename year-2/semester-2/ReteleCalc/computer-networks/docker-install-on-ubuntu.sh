#!/bin/bash
if getent passwd student > /dev/null 2>&1; then
    echo "User student exists"
else
    sudo adduser --disabled-password --gecos "" student
fi

export DEBIAN_FRONTEND=noninteractive

export DOCKER_CONFIG=${DOCKER_CONFIG:-$HOME/.docker}
mkdir -p $DOCKER_CONFIG/cli-plugins


sudo apt update && \
sudo apt install -y build-essential \
                    vim \
                    net-tools \
                    arp-scan \
                    python3 \
                    python3-pip \
                    tcpdump \
                    ethtool \
                    nmap \
                    traceroute \
                    tmux \
                    netcat \
                    inetutils-* && \
sudo pip install scapy && \
sudo apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release \
    software-properties-common  && \
sudo apt-get update && \
sudo apt-get install ca-certificates curl && \
sudo install -m 0755 -d /etc/apt/keyrings && \
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc && \
sudo chmod a+r /etc/apt/keyrings/docker.asc && \
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null && \
sudo apt-get update && \
sudo apt-get -y install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin && \
curl -SL https://github.com/docker/compose/releases/download/v2.26.1/docker-compose-linux-x86_64 -o $DOCKER_CONFIG/cli-plugins/docker-compose
chmod +x $DOCKER_CONFIG/cli-plugins/docker-compose && \
sudo usermod -aG docker $USER && \
sudo usermod -aG docker student && \
sudo passwd -d student && \
newgrp docker && \
echo "DONE"