import sys
sys.stdin = open("in1.txt", "r")

def solve(l):
    cnt  = 1
    ep = x[0]
    for i in range(1, N):
        if x[i]- ep >= l:
            cnt += 1
            ep = x[i]
    return cnt
if __name__ == "__main__":
    N , C = map(int, input().split())
    x = list(int(input()) for _ in range(N))

    x.sort()
    start = x[0]
    end = x[-1]
    res = 0
    while start <= end:
        mid = (start + end) // 2
        if solve(mid) >= C:
            res = mid
            start = mid+1
        else:
            end = mid -1
    print(res)