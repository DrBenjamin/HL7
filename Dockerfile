# app/Dockerfile
FROM python:3.11

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    libmemcached11 \
    libmemcachedutil2 \
    build-essential \
    libmemcached-dev \
    libz-dev \
    libxml2-dev \
    zlib1g-dev \
    libicu-dev \
    g++ \
    python3-dev \
    espeak \
    pkg-config && rm -rf /var/lib/apt/lists/*

RUN python -m pip install --upgrade pip
RUN python -m pip install --upgrade setuptools wheel

WORKDIR /app
RUN git clone https://github.com/DrBenjamin/HL7/ .
#COPY images /app/images

RUN python -m pip install --upgrade -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["python", "-m", "streamlit", "run", "HL7v2.py", "--server.port=8501"]