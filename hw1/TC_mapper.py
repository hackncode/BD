#!/usr/bin/env python3
# total_count_mapper.py
import sys
for line in sys.stdin:
    word, count = line.strip().split('\t')
    count = int(count)
    print(f"{word}\t{count}")
    print(f"__TOTAL__\t{count}")
