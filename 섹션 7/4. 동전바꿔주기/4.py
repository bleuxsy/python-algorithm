import sys
sys.stdin = open("in1.txt", "r")
def dfs(L, total):
    global res
    if L == k :
        if total == T:
            res += 1

    else:
        for i in range(mylist[L][1]+1):
            dfs(L+1, total+(mylist[L][0] * i))


if __name__ == "__main__":
    T = int(input())
    k = int(input())

    res = 0

    mylist =[list(map(int, input().split())) for _ in range(k)]
    mylist.sort(key = lambda x : -x[0])
    print(mylist)
    dfs(0,0)
    print(res)