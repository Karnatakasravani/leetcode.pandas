# cook your dish here
n=int(input())
for _ in range(1,n+1):
    r1,r2,r3,r4,r5=map(int,input().split())
    l=[r1,r2,r3,r4,r5]
    cnt=0
    for i in l:
        if i==1:
            cnt+=1
    if cnt>=4:
        print("YES")
    else:
        print("NO")
    
