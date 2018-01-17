#!/bin/sh

mkdir -p cpp/build
cd cpp/build
cmake ..
make -j4