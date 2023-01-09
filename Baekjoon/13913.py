from collections import deque

MAX=100000
n,k=map(int,input().split())
v=[0]*(MAX+1)
route=[0]*(MAX+1)

def show_route(x):
    
    l=[]
    
    for _ in range(v[x]+1):
        l.append(x)
        x=route[x]
        
    print(' '.join(map(str,l[::-1])))


def bfs():
    q=deque()
    q.append(n)
    while q:
        x=q.popleft()
        
        if x==k:
            print(v[x])
            show_route(x)
            return
        for nx in (x+1,x-1,x*2):
            if 0<=nx<=MAX and v[nx]==0:
                v[nx]=v[x]+1
                route[nx]=x
                q.append(nx)
                
bfs()
            