# ベースイメージ
FROM alpine:3.13
# 参考：https://hub.docker.com/_/alpine

# 作成者
MAINTAINER jumborin

# イメージラベル
LABEL version="1.0"
LABEL description="テスト。XXのサーバ"

# インストール
# RUN apt-get update
# RUN apt-get install -y apache2
# RUN apt-get install -y git

RUN apk update
RUN apk add bash
RUN apk add apache2
RUN apk add git


# 各環境変数を設定
ENV USER jumborin
ENV HOME /home/${USER}
ENV SHELL /bin/bash
ENV PASS p@ssw0rd

# 一般ユーザーアカウントを追加
RUN useradd -m ${USER}

# 一般ユーザーにsudo権限を付与
RUN gpasswd -a ${USER} sudo

# 一般ユーザーのパスワード設定
RUN echo "${USER}:${PASS}" | chpasswd

