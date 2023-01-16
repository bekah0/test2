from collections import deque

import sys

input=sys.stdin.readline

n = int(input())
l=deque()
while True :
    a = int(input())
    if a == -1 :
        break
    
    if a == 0 :
        l.popleft()
    
    elif len(l) < n :
        l.append(a)
if l :
    print(*l) #원소만 출력
else:
    print("empty")