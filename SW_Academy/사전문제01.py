import sys
sys.setrecursionlimit(10**4)
T=int(input())
for test_case in range(T+1):
    r,c=map(int,input().split())
    f=[list(input()) for _ in range(r)]
    v=[]
    res=0
    
    def dfs(x,y,v,d):
        global res
        res=max(d,res)
        v.append(f[y][x])
        
        for (nx,ny) in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
            if 0<=nx<c and 0<=ny<r:
                if f[ny][nx] not in v:
    
                    dfs(nx,ny,v,d+1)
                    v.pop(v.index(f[ny][nx]))
        
    
    dfs(0,0,v,1)
    print("#%d %d"%(test_case,res))
        