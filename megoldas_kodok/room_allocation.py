# Room Allocation
# https://cses.fi/problemset/task/1164/

import heapq
import sys

n = int(sys.stdin.readline().strip())

customers = []
for i in range(n):

    a, b = map(int, sys.stdin.readline().strip().split())
    customers.append((a, b, i))

customers.sort(key=lambda x: x[0])

room_allocations = [0] * n

free_rooms = [] 

available_room_ids = []
for i in range(1, n + 1):
    heapq.heappush(available_room_ids, i)

max_rooms_needed = 0

for arrival, departure, original_index in customers:
    if free_rooms and free_rooms[0][0] < arrival:
        old_departure, room_id = heapq.heappop(free_rooms)
        room_allocations[original_index] = room_id
        heapq.heappush(free_rooms, (departure, room_id))
    else:
        room_id = heapq.heappop(available_room_ids)
        max_rooms_needed = max(max_rooms_needed, room_id)
        room_allocations[original_index] = room_id
        heapq.heappush(free_rooms, (departure, room_id))

print(max_rooms_needed)
print(*(room_allocations))