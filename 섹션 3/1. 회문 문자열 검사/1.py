import sys
sys.stdin = open("in1.txt", "r")

if __name__ == "__main__":
    N = int(input())
    for _ in range(N):
        word =input()
        word = word.upper()
        i=0
        j=len(word)-1
        while True:
            if i == len(word)-1:
                print("YES")
                break
            if word[i] ==word[j]:
                i += 1
                j -= 1
            else:
               print("NO")
               break