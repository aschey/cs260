#!/bin/bash
echo "making stooge sort"
python3 ../sort.py stooge -1 1000 10 10 0
python3 ../sort.py stooge -1 1000 10 10 2000
echo "making insertion sort"
python3 ../sort.py insertion -1 10000 10 10 0
python3 ../sort.py insertion -1 10000 10 10 20000
echo "making selection sort"
python3 ../sort.py selection -1 10000 10 10 0
python3 sort.py selection -1 10000 10 10 20000
echo "making merge sort"
python3 ../sort.py merge -1 10000 10 10 0
python3 ../sort.py merge -1 10000 10 10 20000
echo "making quick sort"
python3 ../sort.py quick -1 10000 10 10 0
python3 ../sort.py quick -1 10000 10 10 20000
