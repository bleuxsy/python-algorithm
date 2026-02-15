import sys

sys.stdin = open("in1.txt", "r")
def dfs(L):
    global res
    if L == N:
        cha = max(money) - min(money)
        if cha < res:
            tmp = set()
            for x in money:
                res.add(x)
            if len(res) == 3:
                res = cha

    else:
        for i in range(3):
            money[i] += coin[L]
            dfs(L+1)
            money -= coin[L]



if __name__ == "__main__":
    N = int(input())
    coin = [int(input()) for _ in range(N)]

    money = [0] * 3
    dfs(0)
    print(res)
