"""
@author: Downsidelama
"""

ids = list()

with open('input.txt') as f:
    for line in f:
        ids.append(line.strip('\n'))

for i in range(len(ids)):
    for j in range(i + 1, len(ids)):
        not_match = 0
        not_match_pos = 0
        for char in range(len(ids[i])):
            if ids[i][char] != ids[j][char]:
                not_match += 1
                not_match_pos = char
        if not_match == 1:
            print(ids[i][:not_match_pos] + ids[i][not_match_pos + 1:])
