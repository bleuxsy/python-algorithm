import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0
s = 0
total = 0

for e in range(N):
    total += A[e]

    while total > M:
        total -= A[s]
        s += 1

    if total == M:
        cnt += 1

print(cnt)