def can_complete_ass(x,y,z):
    t_min=x*y
    t_min_per_day=24*60
    if t_min <= z*t_min_per_day:
        return "YES"
    else:
        return "NO"
x,y,z=map(int,input().split())
res=can_complete_ass(x,y,z)
print(res)
