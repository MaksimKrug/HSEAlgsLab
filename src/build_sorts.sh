#!/bin/bash
# gcc -c -fPIC invert_in_Zp_Ferma.cpp -o invert_in_Zp_Ferma.o;
# gcc invert_in_Zp_Ferma.o -shared -o invert_in_Zp_Ferma.dll;

g++ -fPIC -shared -o RadixSort.so RadixSort.c;

echo "Done"