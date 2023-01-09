"""n=int(input())
wlist=[]
for _ in range(n):
    word=input()
    wlist.append(word)
wlist2=wlist

for word in wlist2:
    sw=True
    for i in range(len(word)):
        for j in range(i,len(word)):
            print(word,word[i],word[j])
            if i == j:
                continue
            #print(word,word[i],word[j])
            if word[i] == word[j] and sw==True:
                wlist.remove(word)
                sw=False

print(len(wlist))
print(wlist)
"""
"""
N = int(input())
result = N
for i in range(0,N):
    word=input()
    for j in range(0,len(word)-1):
        if word[j]==word[j+1]:
            continue
        if word[j] in word[j+1:]:
            result-=1
            break
print(result)"""
"""
clist=['z=' , 's=' , 'nj' , 'lj' , 'd-' , 'dz=' , 'c-' , 'c=']
word=list(input())

count=len(word)
for i in range(len(word)-1):
    if word[i]+word[i+1] in clist:
        count-=1

    if i==len(word)-2:
        continue
    if word[i]+word[i+1]+word[i+2] =='dz=':
        count-=1

print(count)
"""

"""n=int(input())
nlist=[]
for _ in range(n):
    nlist.append(int(input()))

nlist.sort()
for i in nlist:
    print(i)"""

"""n,m=map(int,input().split())

def gcd(a,b):
    while b>0:
        a,b=b,a%b
    return a

def lcm(a,b):
    return a*b // gcd(a,b)


print(gcd(n,m))
print(lcm(n,m))
"""


"""n=list(input())
n.sort(reverse=True)
for i in n:
    print(i, end='')"""
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
    print(rank, end=" ")"""
"""
n=int(input())
nlist=[]
for _ in range(n):
    nlist.append(int(input()))
nlist.sort()
for i in nlist:
    print(i)
"""













































