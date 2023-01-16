from collections import deque

import sys

input=sys.stdin.readline

n = int(input())
q=deque()
for i in range (n) :
    l=list(input().split())

    if l[0]=="push" :
        q.append(l[1])
    elif l[0] == "pop" :
        if q :
            print(q.popleft())
        else :
            print(-1)
    elif l[0] == "size" :
        print(len(q))
    elif l[0] == "empty" :
        if q :
            print(0)
        else :
            print(1)
    elif l[0] == "front" :
        if q :
            print(q[0])
        else :
            print(-1)
    elif l[0] == "back" :
        if q :
            print(q[-1])
        else :
            print(-1)

            
