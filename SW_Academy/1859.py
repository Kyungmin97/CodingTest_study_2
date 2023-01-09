"""

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n=int(input())
    price=list(map(int,input().split()))
    
    result=0
    while(price):
        
        pos=price.index(max(price))
        pre,price=price[:pos],price[pos:]
        x=price.pop(0)
        for i in pre:
            result+=(x-i)
    
    print('#%d %d'%(test_case,result))
    # ///////////////////////////////////////////////////////////////////////////////////

"""

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n=int(input())
    price=list(map(int,input().split()))
    
    result=0
    max_num=0
    for i in range(len(price)-1,-1,-1):
        
        if price[i]>max_num:
            max_num=price[i]
        else:
            result+=max_num-price[i]
        
    
    print('#%d %d'%(test_case,result))
    # ///////////////////////////////////////////////////////////////////////////////////
