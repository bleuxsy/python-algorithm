import sys
sys.stdin = open("in1.txt", "r")

if __name__ == "__main__":
    N = int(input())
    score = list(map(int, input().split()))
    print(score)
    avg = sum(score)//N

    sscore = []
    for i in score:
        sscore.append(abs(i-N))
    print(sscore)
    minvalue = 10000
    cnt = []
    for i,j in enumerate(sscore):
        if j < minvalue:
            minvalue = j

    m = sscore.index(minvalue)

    print(avg)
    print(m)
