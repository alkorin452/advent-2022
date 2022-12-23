from aocd import get_data

input = get_data(day=1, year=2022)
split = input.split('\n\n')

maximum = 0

for elf in split:
    local_max = sum(int(calorie) for calorie in elf.split('\n'))
    maximum = max(maximum, local_max)

print(maximum)