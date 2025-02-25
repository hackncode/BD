#!/usr/bin/env python3
import sys
total_count = 0
word_counts = {}
for line in sys.stdin:
    key, value = line.strip().split('\t')
    count = int(value)
    if key == "__TOTAL__":
        total_count += count
    else:
        if key in word_counts:
            word_counts[key] += count
        else:
            word_counts[key] = count
print(f"__TOTAL__\t{total_count}")
for word, count in word_counts.items():
    print(f"{word}\t{count}")
