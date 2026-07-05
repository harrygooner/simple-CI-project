FROM jenkins/inbound-agent:jdk17

USER root

RUN apt-get update && apt-get install -y --no-install-recommends \
    docker.io \
    python3 \
    python3-pip \
    python3-venv \
    curl \
    git \
    ca-certificates \
    tar \
    gzip \
    && rm -rf /var/lib/apt/lists/*

# Install kubectl
RUN curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" \
    && chmod +x kubectl \
    && mv kubectl /usr/local/bin/kubectl

# Install Helm 3
RUN curl -fsSL https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash