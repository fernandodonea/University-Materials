FROM ubuntu:24.04

RUN apt-get update && apt-get install -y --no-install-recommends \
    cmake \
    g++ \
    make \
    ninja-build \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .

RUN cmake -S . -B build -DCMAKE_BUILD_TYPE=Release \
 && cmake --build build --parallel

# rulam implicit inputul din directory
CMD ["./build/AA_Laborator_Tema", "data/input.txt"]

