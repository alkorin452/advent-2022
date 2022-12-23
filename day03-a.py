from aocd import get_data

'''
7826
'''

input = get_data(day=3, year=2022)

total = 0
for rucksack in input.split('\n'):
    comp1, comp2 = set(rucksack[:len(rucksack)//2]), set(rucksack[len(rucksack)//2:])
    error = list(comp1.intersection(comp2))

    if error:
        error_char = error[0]
        base_char = 'A' if error_char.isupper() else 'a'

        value = (ord(error_char) - ord(base_char)) + 1

        if error_char.isupper():
            value += 26


        total += value
        print(f'Found error {error_char} in halves: {comp1} | {comp2}, base char= {base_char}, value = {value}. total = {total}')

print(total)