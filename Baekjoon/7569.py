from collections import deque
import sys



m,n,h=map(int,input().split())
arr=[]
for _ in range(h):
    arr2=[]
    for _ in range(n):
        row = list(map(int,sys.stdin.readline().split()))
        arr2.append(row)
    arr.append(arr2)

dx=[0,0,0,0,-1,1]
dy=[0,0,-1,1,0,0]
dz=[-1,1,0,0,0,0]



def zerocheck(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if 0 in arr[i][j]:
                return True
    return False

def foo(arr):
    
    q=deque()
    temp=set([])

    for k in range(h):
        for j in range(n):
            for i in range(m):
                if arr[k][j][i] == 1:
                    q.append((i,j,k))

    if not zerocheck(arr):
        return(0)

    cnt=1
    while q:
        if cnt>200:
            return(-1)
        

        x,y,z=q.popleft()   
        
        for i in range(6):
            nx=x+dx[i]
            ny=y+dy[i]
            nz=z+dz[i]
            if 0<=nx<m and 0<=ny<n and 0<=nz<h and arr[nz][ny][nx]==0:
                temp.add((nx,ny,nz))
                arr[nz][ny][nx]=1

        if not q:
            if not zerocheck(arr):
                return(cnt)
            for i in temp:
                q.append(i)
            cnt+=1
            

print(foo(arr))





