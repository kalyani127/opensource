def can_ach_marks(N,X,Y):
    max_p_marks=N*X
    return "YES" if Y <= max_p_marks and Y%X==0 else "NO"
N,X,Y=map(int,input().split())
res=can_ach_marks(N,X,Y)
print(res)
