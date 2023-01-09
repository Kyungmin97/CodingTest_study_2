from collections import deque

v=dict()
v[(1,0)]=0
s=int(input())

def bfs():
    q=deque()
    q.append((1,0))
    
    while q:
        x,c=q.popleft()
        if x == s:
            print(v[(x,c)])
            return
        
        for (nx,nc) in ((x,x),(x+c,c),(x-1,c)):
            if (nx,nc) not in v.keys() and nc>=0 and nx>=1:
                v[(nx,nc)]=v[(x,c)]+1
                q.append((nx,nc))
        
                
bfs()