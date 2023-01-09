"""
n=int(input())
nlist=list(map(int,input().split()))
count=n

for i in nlist:
    for j in range(2,i):
        if i/j == i//j:
            count-=1
            break
print(count-nlist.count(1))
"""
"""
n=int(input())
nlist=[]

for _ in range(n):
    m=input().split()
    if m[0]=='push':
        nlist.append(m[1])

    elif m[0]=='pop':
        try:
            num=nlist.pop()
            print(num)
        except:
            print(-1)

    elif m[0]=='size':
        print(len(nlist))

    elif m[0]=='empty':
        if len(nlist) >0:
            print(0)
        else:
            print(1)

    elif m[0]=='top':
        try:
            print(nlist[-1])
        except:
            print(-1)
"""
"""
n=int(input())
nlist=[]

for _ in range(n):
    count=0
    sw=True
    m=list(input())
    for i in m:
        if i=='(':
            count+=1
        elif i==')' and count>0:
            count-=1
        else:
            print("NO")
            sw=False
            break
    if sw==True and count==0:
        print("YES")
    elif count !=0:
        print("NO")
"""
"""
n=int(input())
nlist=list(map(int,input().split()))
nlist.sort()
m=int(input())
mlist=list(map(int,input().split()))

def binary(t):
    left=0
    right=n-1

    while left <= right:
        mid=(left+right)//2
        if nlist[mid]==t:
            return True
        if t<nlist[mid]:
            right=mid-1
        elif t>nlist[mid]:
            left=mid+1


for i in mlist:
    if binary(i):
        print(1)
    else:
        print(0)
"""





































