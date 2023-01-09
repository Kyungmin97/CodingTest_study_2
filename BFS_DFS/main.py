
#DFS Part
#1
"""
def dfs(graph, v, visited):
    visited[v]=True
    #방문처리
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            #재귀 호출

graph=[
    [],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]
]

visited=[False]*9
dfs(graph,1,visited)
"""

#BFS Part
#2
"""
from collections import deque
def bfs(graph, start, visited):
    queue=deque([start])
    visited[start]=True
    #방문처리
    while queue:
        v=queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
                #재귀 호출


graph=[
    [],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]
]

visited=[False]*9
bfs(graph,1,visited)

"""
#3
"""

n,m=map(int,input().split())

graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    if x>=n or x<0 or y<0 or y>=m:
        return False
    if graph[x][y]==1:
        return False

    graph[x][y]=1
    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y+1)
    dfs(x,y-1)
    return True

result=0
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            result+=1
print(result)
"""
#4 1260

"""
from collections import deque

n,m,v=map(int,input().split())

graph=[]

for i in range(m):
    graph.append(list(map(int,input().split())))

def dfs(graph,v,visited):
    print(v, end=' ')
    visited[v]=True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

def bfs(graph, start, visited):
    queue=deque([start])
    visited[start]=True
    #방문처리
    while queue:
        v=queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
                #재귀 호출



visited=[False] * (n+1)

for _ in range(m):
    graph[a].append(b)


for i in range(1,n+1):
    graph[i].sort()

dfs(v)
visited=[False] * (n+1)
print()
bfs(v)
"""

#5 2178
"""
from collections import deque

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
"""

#6 2667
"""
from collections import deque
dy=[0,0,-1,1]
dx=[-1,1,0,0]

def bfs(graph,a,b):
    n=len(graph)
    queue=deque()
    queue.append((a,b))
    graph[a][b]=0
    count=1

    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx,ny))
                count += 1
    return count

n=int(input())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

cnt=[]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt.append(bfs(graph,i,j))

cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])
"""

#7 2606 DFS
"""
n=int(input())
m=int(input())
graph=[[]*n for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
visited=[0] * (n+1)
def dfs(start):
    global cnt
    visited[start] = 1
    for i in graph[start]:
        if visited[i]==0:
            dfs(i)
            cnt += 1

dfs(1)
print(cnt)
"""

#8 1012
"""
from collections import deque

dx=[0,0,1,-1]
dy=[1,-1,0,0]

t=int(input())

def bfs(graph,a,b):
    queue = deque()
    queue.append((a,b))
    graph[a][b] = 0

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx,ny))
    return

for i in range(t):
    cnt = 0
    n,m,k=map(int,input().split())
    graph = [[0]*m for _ in range(n)]

    for j in range(k):
        x,y = map(int,input().split())
        graph[x][y]=1

    for a in range(n):
        for b in range(m):
            if graph[a][b] == 1:
                bfs(graph,a,b)
                cnt += 1
    print(cnt)
"""

#9 7576
"""
from collections import deque

m,n=map(int,input().split())
graph=[]
queue = deque([])
for i in range(n):
    graph.append(list(map(int,input().split())))

    for j in range(m):
        if graph[i][j]==1:
            queue.append([i,j])

dx, dy = [-1,1,0,0], [0,0,-1,1]

def bfs():
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx, ny = dx[i]+x, dy[i]+ y
            if n>nx>=0 and m>ny>=0 and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx,ny])

bfs()
res=0
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))
print(graph)
print(res-1)
"""

#10 1697
"""
MAXNUM=100000
from collections import deque
n,k=map(int,input().split())
visited=[False]*(MAXNUM+1)

def bfs(v):
    count=0
    q=deque()
    q.append([v,count])

    while q:
        x=q.popleft()
        current=x[0]
        count=x[1]

        if visited[current] ==False:
            visited[current]=True

            if current == k:
                return count

            count += 1

            if current * 2 <= MAXNUM:
                q.append([current*2,count])
            if current +1 <= MAXNUM:
                q.append([current+1,count])
            if current -1 >= 0:
                q.append([current-1,count])

    return count

print(bfs(n))
"""

#11 11724
"""
from collections import deque

n,m=map(int,input().split())
visited=[False] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(v):
    q=deque()
    q.append(v)

    while q:
        x=q.popleft()
        if visited[x] == False:
            visited[x]=True
            for i in graph[x]:
                q.append(i)

cnt=0
for i in range(1,n+1):
    if visited[i]==False:
        bfs(i)
        cnt+=1

print(cnt)
"""

#12 14502
"""
from collections import deque
import copy

n,m=map(int,input().split())
graph=[]
dx,dy=[0,0,-1,1],[-1,1,0,0]

for i in range(n):
    graph.append(list(map(int,input().split())))

def bfs():
    q = deque()
    tmp_graph=copy.deepcopy(graph)
    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j] == 2:
                q.append((i,j))
    while q:
        x,y=q.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx<0 or ny<0 or nx>=n or ny>= m:
                continue
            if tmp_graph[nx][ny] == 0:
                tmp_graph[nx][ny] = 2
                q.append((nx,ny))

    global answer
    cnt=0

    for i in range(n):
        cnt += tmp_graph[i].count(0)

    answer = max(answer,cnt)

def makewall(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                makewall(cnt+1)
                graph[i][j] = 0

answer=0
makewall(0)
print(answer)
"""

#13 4963
"""
from collections import deque

while True:
    w,h=map(int,input().split())
    if w==0 and h==0:
        break
    island = [list(map(int,input().split())) for _ in range(h)]

    dx=[-1,-1,0,1,1,1,0,-1]
    dy=[0,1,1,1,0,-1,-1,-1]

    q=deque()
    cnt=0
    for i in range(h):
        for j in range(w):
            if island[i][j] == 1:
                q.append((i,j))
                island[i][j] = 2

                while q:
                    cx,cy = q.popleft()
                    for k in range(8):
                        nx=cx+dx[k]
                        ny=cy+dy[k]
                        if 0<=nx<h and 0<=ny<w:
                            if island[nx][ny] == 1:
                                q.append((nx,ny))
                                island[nx][ny]=2
                else:
                    cnt += 1
    print(cnt)
"""

#14 2468 // dfs
"""
import sys
sys.setrecursionlimit(100000)

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x,y,h):
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if(0<=nx<N) and (0<=ny<N):
            if arr[nx][ny]>h and done[nx][ny]==0:
                done[nx][ny]=1
                dfs(nx,ny,h)

N=int(input())
arr=[list(map(int,input().split())) for _ in range(N)]
ans=0

for k in range(max(map(max,arr))):
    cnt=0
    done=[[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] > k and done[i][j] == 0:
                done[i][j] = 1
                cnt+=1
                dfs(i,j,k)

    ans=max(ans,cnt)
print(ans)
"""

#15 10026
"""
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(x,y):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    visited[y][x]=1
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if (0<=nx<=n) and(0<=ny<n) and arr[y][x]==arr[ny][nx] and visited[ny][nx]==0:
            dfs(nx,ny)

n=int(input())
arr=[list(map(str,input())) for _ in range(n)]
visited=[[0]*n for _ in range(n)]
cnt1=0
for i in range(n):
    for j in range(n):
        if visited[i][j]==0:
            cnt1+=1
            dfs(j,i)
for i in range(n):
    for j in range(n):
        if arr[i][j]=='R':
            arr[i][j]='G'
cnt2=0
visited=[[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j]==0:
            cnt2+=1
            dfs(j,i)
print(cnt1,cnt2)
"""

#16 1987
"""
import sys
sys.setrecursionlimit(10000)

def dfs(x,y,cnt):
"""

#17 BruteForce 1065
"""
def hansu(num):
    cnt=0
    for i in range(1,num+1):
        nlist=list(map(int,str(i)))
        if i < 100:
            cnt+=1
        elif nlist[0]-nlist[1] == nlist[1]-nlist[2]:
            cnt+=1
    return cnt
num=int(input())
print(hansu(num))
"""
#18 4673
"""
def notself(num):
    answer=[i for i in range(1,num+1)]
    for i in range(1,10):
        if i+i in answer:
            answer.remove(i+i)

    for i in range(10,100):
        nlist=list(map(int,str(i)))
        if i+nlist[0]+nlist[1] in answer:
            answer.remove(i+nlist[0]+nlist[1])

    for i in range(100,1000):
        nlist=list(map(int,str(i)))
        check=i+nlist[0]+nlist[1]+nlist[2]
        if check in answer:
            answer.remove(check)

    for i in range(1000, 10000):
        nlist = list(map(int, str(i)))
        check = i + nlist[0] + nlist[1] + nlist[2]+nlist[3]
        if check in answer:
            answer.remove(check)
    for i in range(len(answer)):
        print(answer[i])

notself(10000)
"""

#19 2798
"""
def fun1():
    nlist=list(map(int,input().split()))
    nlist.sort(reverse=True)
    answer=0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if nlist[i]+nlist[j]+nlist[k]>m:
                    continue
                else:
                    answer=max(answer,nlist[i]+nlist[j]+nlist[k])
    print(answer)

n,m=map(int,input().split())
fun1()
"""

#20 2231
"""
num=int(input())
answer=0
for n in range(1,num):
    k=n
    for i in str(n):
        n+=int(i)
    if n == num:
        answer=k
        break
print(answer)
"""

#21 7568
"""
n=int(input())
nlist=[]
for _ in range(n):
    w,h=map(int,input().split())
    nlist.append((w,h))
for i in nlist:
    rank=1
    for j in nlist:
        if i[0] < j[0] and i[1] < j[1]:
            rank+=1
    print(rank, end=" ")
"""

#22 2309
"""
nlist=[]
for _ in range(9):
    nlist.append(int(input()))

all=sum(nlist)
result=all
sw=False
for i in range(9):
    for j in range(i+1,9):
        n1=nlist[i]
        n2=nlist[j]
        result=result-n1-n2
        if result == 100:
            nlist.remove(n1)
            nlist.remove(n2)
            sw=True
            break
        else:
            result=all
    if sw==True:
        break
nlist.sort()
for i in nlist:
    print(i)
"""

#23 2839
"""
n=int(input())
count=0

count+=n//5
n=n%5
if n==1 and count>0:
    count+=1
elif n==2 and count>1:
    count+=2
elif n==3:
    count+=1
elif n==4 and count>0:
    count+=2
elif n==0:
    count+=0
else:
    count=-1

print(count)
"""

#24 11399
"""
n=int(input())
nlist = list(map(int,input().split()))
nlist.sort()
answer=0
wtime=0
for i in nlist:
    wtime+=i
    answer+=wtime
    #print("wtime: {0}\tanswer: {1}".format(wtime,answer))
print(answer)
"""

#25 11047
"""
n,k=map(int,input().split())
nlist=[]
for _ in range(n):
    nlist.append(int(input()))
count=0
amount=k
nlist.sort(reverse=True)
while amount>0:
    for i in nlist:
        if i<=amount:
            count+=amount//i
            amount=amount%i
print(count)
"""

#26 101855
"""
n=int(input())
nlist=[]
for _ in range(n):
    nlist.append(list(map(int,input().split())))

nlist=sorted(nlist,key=lambda x: x[0])
nlist=sorted(nlist,key=lambda x: x[1])
count=0
end=0
for i in nlist:
    if end<=i[0]:
        count+=1
        end=i[1]
print(count)
"""

#27 1026
"""
#입력
n=int(input())
a=(list(map(int,input().split())))
b=(list(map(int,input().split())))

#계산
answer = 0
for i in range(n):
    answer+=min(a)*max(b)
    a.pop(a.index(min(a)))
    b.pop(b.index(max(b)))

print(answer)
"""

#28 1541
"""
s=input().split('-')

for i in s:
    if '+' in i:
        sum=i.split('+')
        suum=0
        for j in sum:
            suum+=int(j)
        s[s.index(i)]=suum
    else:
        s[s.index(i)]=int(i)

answer=s[0]+s[0]
for i in s:
    answer-=i

print(answer)
"""





