import sys
sys.stdin = open("in1.txt", "r")
def dfs(L , txt):
    global res
    if L == len(word):
        print(txt)
        res +=1
        return

    else:
        if word[L] == '0':
            dfs(L+1, txt)
        else:
            dfs(L + 1 , txt+alphabet[int(word[L]) - 1])
            if L < len(word)-1 and int(word[L] + word[L+1]) < 27:
                dfs(L+2, txt + alphabet[int(word[L]+ word[L+1])-1])




if __name__ == "__main__":
    word = list(input())


    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res = 0

    print(word)
    dfs (0, '')
    print(res)