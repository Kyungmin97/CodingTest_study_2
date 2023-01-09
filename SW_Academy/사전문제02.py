import sys
sys.setrecursionlimit(10**3)

def dfs(d):
    global L,x,y,res
    if d==L+1:
        return
    for nx in y,x:
        if N>res+nx*(10**(L-d)):
            res=res+nx*(10**(L-d))
            dfs(d+1)
            return







T=int(input())
for test_case in range(1,T+1):
    
    
    N,x,y=map(int,input().split())
    f=list(map(int,str(N)))
           
    L=len(f)
    v=[]
    res=0
    
    dfs(1)
    if res==0:
        res=-1

    
    print("#%d %d"%(test_case,res))
        