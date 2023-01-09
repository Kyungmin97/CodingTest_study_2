n=int(input())

for t in range(n):
    res=0
    for i in map(int,input().split()):
        if i%2==1:
            res+=i
    print('#%d %d'%(t+1,res))