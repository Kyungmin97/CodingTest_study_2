
#T = int(input())
T=10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    
    result=0
    length=int(input())
    height=list(map(int,input().split()))
    
    for i in range(2,length-2):
        temp=max(height[i-2],height[i-1],height[i+1],height[i+2])
        if height[i]>temp:
            result+=height[i]-temp
    print("#%d %d"%(test_case,result))
    
    
    # ///////////////////////////////////////////////////////////////////////////////////
