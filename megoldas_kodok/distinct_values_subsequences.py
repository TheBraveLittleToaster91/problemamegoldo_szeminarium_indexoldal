import sys

MOD = 10**9 + 7

n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().strip().split()))

freq = {}

for val in a:
    freq[val] = freq.get(val, 0) + 1

result = 1
for f in freq.values():
    result = (result * (f + 1)) % MOD

result = (result - 1 + MOD) % MOD

print(result)