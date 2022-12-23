from aocd import get_data
from aocd import numbers

input = get_data(day=4, year=2022)

overlap_count = 0

for line in numbers:
    start1 = line[0]
    end1 = line[1] * -1 # Multiply by neg bc the library parses incorrectly
    start2 = line[2]
    end2 = line[3] * -1 # Same as above

    if (start1 <= start2 and start2 <= end1) or (start2 <= end1 and end1 <= end2) or \
        (start2 <= start1 and start1 <= end2) or (start1 <= end2 and end2 <= end1):
        overlap_count += 1

print(overlap_count)