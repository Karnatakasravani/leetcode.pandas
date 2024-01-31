# cook your dish here
t=int(input())
for _ in range(1,t+1):
    n,ch=map(int,input().split())
    l=list(map(int,input().split()))
    # l=[x1,x2,x3,x4]
    L=[]
    for i in l:
        if i>=ch:
            L.append(i%ch)
    if L==[]:
        print(-1)
    else:
        print(min(L))
    
