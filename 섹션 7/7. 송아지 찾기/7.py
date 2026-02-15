import sys
from collections import deque
sys.stdin = open("in1.txt", "r")
# def bfs(now , lev):
#     global res
#     if now > E:
#         if res > lev:
#             res = lev
#         return
#     else:
#         for i in range(3):
#             bfs(now+move[i],lev+1 )


if __name__ == "__main__":
    S , E = map(int, input().split())
    lev = 0
    stack = deque()
    MAX = 100000
    move = [ -1, 1 , 5]
    res = -10000
    stack.append(S)
    visited = [False] * (MAX+1)
    dis = [0] * (MAX+1)
    visited[S] = True
    dis[S] = 0

    while stack:
        now = stack.popleft()
        for next in (now-1, now+1, now+5):
            if 0<next<=MAX:
                if not visited[next] :
                    stack.append(next)
                    visited[next] = True
                    dis[next] = dis[now] +1
        # if not visited[now] :
        #     if now == E:
        #         print(dis[now])
        #         break
        #     else:
        #         for i in [-1, 1, 5]:
        #             nxt = now + i
        #             visited[nxt] = True
        #             dis[nxt] = dis[now] + 1


    print(dis[E])