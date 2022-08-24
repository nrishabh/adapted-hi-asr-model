FROM ubuntu:20.04
RUN date
RUN apt-get update && \
    apt-get install -y -q --no-install-recommends \
    build-essential \
    curl \
    git \
    pkg-config \
    # Libs below are used to install tools
    libssl-dev \
    libtool \
    zlib1g-dev \
    automake \
    autoconf \
    unzip \
    wget \
    # used during mkl installation
    sox \
    gfortran \
    subversion \
    # Needed to kill the server on debug mode.
    lsof \
    libzmq3-dev \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*
