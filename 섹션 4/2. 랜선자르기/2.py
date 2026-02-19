import sys
sys.stdin = open("in1.txt", "r")

def cnnt(length):
    cnt = 0
    for x in lst:
        cnt += x // length
    return cnt

if __name__ == "__main__":
    lst = []
    K, N = map(int, sys.stdin.readline().split())
    for _ in range(K):
        lst.append(int(sys.stdin.readline()))

    res = 0
    s = 1
    e = max(lst)

    while s <= e:
        mid = (s + e) // 2
        if cnnt(mid) >= N:
            res = mid
            s = mid + 1   # 더 크게 가능?
        else:
            e = mid - 1   # 너무 큼, 줄이기

    print(res)