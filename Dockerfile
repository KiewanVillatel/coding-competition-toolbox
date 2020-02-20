# Base image to be pulled
FROM ubuntu:19.10

RUN apt-get update && apt-get clean -y

RUN apt-get install -y \
    git \
    python3-pip \
    python3 \
    bash-completion \
    sudo \
    locales \
    wget \
    net-tools

# Set the locale
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8
ENV LANGUAGE en_US:en


RUN ln -s /usr/bin/pip3 /usr/bin/pip
RUN pip install --upgrade pip

# Install pip requirements
RUN pip install virtualenv

RUN mkdir /virtualenv
WORKDIR /virtualenv
COPY requirements.txt /virtualenv

RUN virtualenv --python=python3 env && \
    . env/bin/activate

RUN . env/bin/activate && pip install -r /virtualenv/requirements.txt


WORKDIR /project