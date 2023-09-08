n=int(input())
arr1=list(map(int,input().split()))
arr1=sorted(arr1)
m=int(input())
arr2=list(map(int,input().split()))


def binarysearch(start,end,x):
    mid=(start+end)//2
    if start > end:
        return 0
    if arr1[mid] == x:
        return 1
    elif arr1[mid] > x:
        return binarysearch(start,mid-1,x)
    else:
        return binarysearch(mid+1,end,x)
    

for x in arr2:
    print(binarysearch(0,n-1,x))
