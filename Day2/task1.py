"""
@author: Downsidelama
"""

two_char = 0
three_char = 0

ids = list()

with open('input.txt') as f:
    for line in f:
        ids.append(line)


def count_in_string(letter, string):
    count = 0
    for char in string:
        if char == letter:
            count += 1
    return count


for line in ids:
    two_chr = False
    three_chr = False
    for i in range(len(line)):
        if line[i] not in line[:i]:
            count_letter = count_in_string(line[i], line[i + 1:])
            if count_letter == 2:
                three_chr = True
            if count_letter == 1:
                two_chr = True

    if two_chr is True:
        two_char += 1
    if three_chr is True:
        three_char += 1

print(two_char * three_char)
