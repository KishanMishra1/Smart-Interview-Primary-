for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    res=0
    for i in range(0,32):
        s=0
        x=1<<i
        for j in range(0,n):
            if (a[j] & x):
                s+=1
        if (s%3!=0):
            res=res|x
    print(res)
