T=int(input())
for i in range(0,T):
    p,r=map(int,input().split())
    if r>=p:
        print('0')
    else:
        print(p-r)
