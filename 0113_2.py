from collections import deque

import sys

input=sys.stdin.readline

n = int(input())
#q=deque()

l= [i for i in range(1,n+1)]
q=deque(l) 

while(len(q)!=1) :
    q.popleft()
    q.append(q.popleft())
   

print(q[0])