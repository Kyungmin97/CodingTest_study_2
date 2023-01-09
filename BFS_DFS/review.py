#from collections import deque
"""
n,m=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input())))
dx=[-1,1,0,0]
dy=[0,0,-1,1]


def bfs(x,y):
    queue=deque()
    queue.append((x,y))

    while queue:
        x,y=queue.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))

    return graph[n-1][m-1]
print(bfs(0,0))
""""""
from collections import deque
n,m=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    q=deque()
    q.append((x,y))

    while q:
        x,y=q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny]==0 or ( nx==0 and ny==0 ):
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                q.append((nx,ny))
    return graph[n-1][m-1]

print(bfs(0,0))
"""
"""
from collections import deque
n=int(input())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    q=deque()
    q.append((x,y))
    count=1
    graph[x][y] = 0

    while q:
        x,y=q.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=0
                count+=1
                q.append((nx,ny))
    return count

nhouse=0
nlist=[]

for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            nlist.append(bfs(i,j))
            nhouse+=1

print(nhouse)
nlist.sort()
for i in nlist:
    print(i)
"""
"""
def dfs(v):
    visited[v]=1
    stack.append(v)
    while stack:
        for i in graph[v]:
            if visited[i]==0:
                visited[i] = 1
                stack.append(v)
                v=i
                break
        else:
            v=stack.pop()
    return sum(visited)-1


n=int(input())
m=int(input())
graph=[[] for i in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited=[0]*(n+1)
stack=[]
print(dfs(1))
""""""
import sys
sys.setrecursionlimit(10000)
dx=[0,0,-1,1]
dy=[-1,1,0,0]

def dfs(x,y):
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if (0<=nx<n) and (0<=ny<m):
            if graph[nx][ny] ==1:
                graph[nx][ny]=-1
                dfs(nx,ny)

t=int(input())
for _ in range(t):
    cnt=0
    m,n,k=map(int,input().split())
    graph=[[0]*m for _ in range(n)]
    for _ in range(k):
        a,b=map(int,input().split())
        graph[b][a]=1

    for i in range(n):
        for j in range(m):
            if graph[i][j] ==1:
                dfs(i,j)
                cnt+=1

    print(cnt)

""""""
n=int(input())

if n>=90:
    a='A'
elif n>=80:
    a='B'
elif n>=70:
    a='C'
elif n>=60:
    a='D'
else:
    a='F'
print(a)

"""

nlist=[i for i in range(1,10000)]

for num in range(1,10000):
    sum=num
    num=str(num)
    for i in num:
        sum+=int(i)

    if sum in nlist:
        nlist.remove(sum)

for i in nlist:
    print(i)


