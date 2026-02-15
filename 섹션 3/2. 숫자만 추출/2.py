import sys
sys.stdin = open("in1.txt", "r")
res =''
if __name__ == "__main__":
    word = list(input())
    for w in word:
        if w.isdigit():
            res+=w

    res = int(res)
    print(res)
    solve =0
    for i in range(1, res+1):
        if res%i == 0:
            solve += 1
    print(solve)