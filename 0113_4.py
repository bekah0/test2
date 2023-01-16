from collections import deque

import sys

input=sys.stdin.readline

n,k = map(int,input().split())
l = deque([i for i in range(1,n+1)])
q = deque()

for i in range(n) :
    c = 0

    while l :
        if c == k-1 :
            q.append(l.popleft())
            break
        l.append(l.popleft())
        c+=1


p=' '.join(list(map(str,q)))

print("<",end='')
for i in range(len(q)-1) :
    print("%d, "%(q[i]),end='')
print("%d>"%q[-1])