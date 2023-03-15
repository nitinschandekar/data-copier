FROM python
# Install OS Modules
RUN  apt update -y && \
    apt install telnet && \
    rm -rf /var/lib/apt/lists/*
# Copy source code
RUN  mkdir /data-copier
COPY src /data-copier/src
COPY requirements.txt /data-copier
# Install Application dependencies
RUN pip install -r /data-copier/requirements.txt