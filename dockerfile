# �x�[�X�C���[�W
FROM alpine:3.13
# �Q�l�Fhttps://hub.docker.com/_/alpine

# �쐬��
MAINTAINER jumborin

# �C���[�W���x��
LABEL version="1.0"
LABEL description="�e�X�g�BXX�̃T�[�o"

# �C���X�g�[��
# RUN apt-get update
# RUN apt-get install -y apache2
# RUN apt-get install -y git

RUN apk update
RUN apk add bash
RUN apk add apache2
RUN apk add git


# �e���ϐ���ݒ�
ENV USER jumborin
ENV HOME /home/${USER}
ENV SHELL /bin/bash
ENV PASS p@ssw0rd

# ��ʃ��[�U�[�A�J�E���g��ǉ�
RUN useradd -m ${USER}

# ��ʃ��[�U�[��sudo������t�^
RUN gpasswd -a ${USER} sudo

# ��ʃ��[�U�[�̃p�X���[�h�ݒ�
RUN echo "${USER}:${PASS}" | chpasswd

