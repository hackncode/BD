#!/usr/bin/env python3
# prob_mapper.py
import sys
total_count = 0
words = []
for line in sys.stdin:
    key, value = line.strip().split('\t')
    
    if key == "__TOTAL__":
        total_count = int(value)
    else:
        words.append((key, int(value)))
words.sort(key=lambda x: x[1], reverse=True)
print(f"__TOTAL__\t{total_count}")
if len(words) >= 15:
    print(f"10\t{word10}\t{count10}")
    print(f"15\t{word15}\t{count15}")