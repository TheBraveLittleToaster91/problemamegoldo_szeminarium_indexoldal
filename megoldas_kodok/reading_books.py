# Reading Books
# https://cses.fi/problemset/task/1631/

import sys

T = list(map(int, sys.stdin.readline().strip().split()))

total_time_sum = sum(T)
max_time = max(T)
minimum_total_time = max(total_time_sum, 2 * max_time)

print(minimum_total_time)