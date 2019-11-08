mkdir -p build/linux/
g++ -w -std=c++11 -pthread -O3 fastBPE/main.cc -IfastBPE -o build/linux/fast
