from aocd import get_data
from aocd import lines
from aocd import numbers

input = get_data(day=5, year=2022)

stacks = [[] for i in range(0, 9)]

# Parse inputs into stacks
for line in lines:
    if line == ' 1   2   3   4   5   6   7   8   9 ':
        break
    for i in range(0, len(line), 4):
        if line[i] == '[':
            stacks[i // 4].append(line[i+1])

for i in range(0, len(stacks)):
    stacks[i] = stacks[i][::-1]


# Exec commands
print(f'Start = {stacks}')
for command in numbers[1:]:
    for i in range(0, command[0]):
        from_stack = command[1] - 1
        to_stack = command[2] - 1

        if stacks[from_stack]:
            crate = stacks[from_stack].pop()
            stacks[to_stack].append(crate)


result = ''
for stack in stacks:
    result += stack[-1]

print(result)
