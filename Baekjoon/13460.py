from collections import deque

n, m = map(int, input().split())
f = [list(input()) for _ in range(n)]
v = set()
found = False
foundb = False
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def no_obstacle(x, y, i,R):
    k = 0
    global found, foundb
    while True:
        if f[y + dy[i] * k][x + dx[i] * k] == 'O':
            if R ==True:
                found = True
            else:
                foundb = True

        if f[y + dy[i] * k][x + dx[i] * k] == '#':
            k -= 1
            break
        k += 1

    return k


def find_ball(c):
    for i in range(n):
        if c in f[i]:
            x = f[i].index(c)
            return x, i
    return -1, -1


def bfs():
    global found, foundb
    q = deque()
    x, y = find_ball('R')
    xb, yb = find_ball('B')
    res = 0
    q.append((x, y, xb, yb, res))
    while q:
        x, y, xb, yb, res = q.popleft()
        v.add((x, y, xb, yb))
        if res>=10:
            break
        #print(x, y, xb, yb, res)
        for i in range(4):
            k = no_obstacle(x, y, i,True)
            nx = x + dx[i] * k
            ny = y + dy[i] * k
            kb = no_obstacle(xb, yb, i,False)
            nxb = xb + dx[i] * kb
            nyb = yb + dy[i] * kb

            #print(nx, ny, nxb, nyb,found,foundb)
            if foundb == True:
                found = False
                foundb = False
                continue
            elif found == True:
                return res+1

            if nx == nxb and ny == nyb:
                if k > kb:
                    nx = x + dx[i] * (k - 1)
                    ny = y + dy[i] * (k - 1)
                else:
                    nxb = xb + dx[i] * (kb - 1)
                    nyb = yb + dy[i] * (kb - 1)

            if (nx == x and ny == y and nxb == xb and nyb == yb):
                continue
            if (nx, ny, nxb, nyb) in v:
                continue
            q.append((nx, ny, nxb, nyb, res + 1))
    return -1


print(bfs())

