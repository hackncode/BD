#!/usr/bin/env python3
import sys
id_counter = 0
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    try:
        neg_count, word = line.split('\t', 1)
    except ValueError:
        continue
    id_counter += 1
    print(f"{id_counter}\t{word}")
