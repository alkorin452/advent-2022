from aocd import get_data
from aocd import lines

total = 0

for index in range(0, len(lines), 3):
    ruck1 = set(lines[index])
    ruck2 = set(lines[index+1])
    ruck3 = set(lines[index+2])

    badge = list(ruck1.intersection(ruck2).intersection(ruck3))[0]
    print(badge)

    base_char = 'A' if badge.isupper() else 'a'
    value = (ord(badge) - ord(base_char)) + 1

    if badge.isupper():
        value += 26

    total += value

print(total)