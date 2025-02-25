#!/usr/bin/env python3
# prob_reducer.py
import sys
total_count = 0
word_data = {}
for line in sys.stdin:
    parts = line.strip().split('\t')
    if parts[0] == "__TOTAL__":
        total_count = int(parts[1])
    else:
        id_num = int(parts[0])
        word = parts[1]
        count = int(parts[2])
        word_data[id_num] = (word, count)
for id_num in sorted(word_data.keys()):
    word, count = word_data[id_num]
    probability = count / total_count if total_count > 0 else 0
    print(f"Word #{id_num}: {word}, Probability: {probability:.6f}")
