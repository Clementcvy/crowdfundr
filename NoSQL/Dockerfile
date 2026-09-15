FROM mongo:7

RUN apt-get update \
    && apt-get install -y --no-install-recommends python3 \
    && rm -rf /var/lib/apt/lists/*

ENV TERM=xterm

WORKDIR /app

COPY NoSQL/Application ./NoSQL/Application

CMD ["python3", "NoSQL/Application/main.py"]
