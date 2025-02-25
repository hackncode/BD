#!/usr/bin/env python3
import sys
MAX = 1000000000
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    try:
        word, count_str = line.split('\t', 1)
        count = int(count_str)
    except ValueError:
        continue
    key = MAX - count
    print(f"{key:010d}\t{word}")
