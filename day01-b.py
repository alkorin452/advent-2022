from aocd import get_data
import heapq

input = get_data(day=1, year=2022)
split = input.split('\n\n')

heap = []
heapq.heapify(heap)

for elf in split:
    local_sum = sum(int(calorie) for calorie in elf.split('\n'))
    heapq.heappush(heap, local_sum * -1)

total = sum(int(total_cal) for total_cal in heapq.nsmallest(3, heap)) * -1

print(heap)
print(total)