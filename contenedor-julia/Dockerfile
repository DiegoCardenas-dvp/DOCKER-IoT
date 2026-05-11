FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
    build-essential \
    g++ \
    gnuplot \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /usr/src/app
COPY . .
# Compila y genera la imagen usando las carpetas internas
CMD g++ src/main.cpp -o bin/programa && ./bin/programa && gnuplot scripts/plot.gp
