import sys
sys.stdin = open("in1.txt", "r")
res =''
def solve(c):
    cnt = 1
    sum = 0
    for x in song:
        if sum+x > c:
            cnt += 1
            sum = x
        else:
            # 저장할 수 있을때
            sum += x
    return cnt
if __name__ == "__main__":
    N , M = map(int, input().split())
    song = list(map(int, input().split()))

    start = 1
    # 정답이 될 수 있는 최소 용량
    end = sum(song)
    # 정답이 될 수 있는 최대 용량
    mid = (start+end)//2
    # 해당 범위 안에 정답이 있다고 가정하고, 가운데 값을 찍어서 테스트
    i = 0
    lst = []
    res = 0
    while start <= end:
        mid = (start + end) // 2
        if solve(mid) <= M:
            res = mid
            end = mid -1
        else:
            start = mid + 1
    print(res)


    # start = 0
    # end = N-1
    # total = 0
    # for f in range(len(flag)):
    #     if total == 0:
    #         total = sum(song[flag[f]:flag[f+1]])
    #     else:
    #         if total > sum(song[flag[f]:flag[f+1]]):
    #             flag[f] +=1
    #         elif total < sum(song[flag[f]:flag[f+1]]):
    #             flag[f] -= 1


