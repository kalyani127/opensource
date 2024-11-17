def cal_req_plane(n,m):
    total_cap=n*100
    require_cap=m
    addition_plane_need=(require_cap - total_cap) // 100
    if (require_cap - total_cap) % 100>0:
        addition_plane_need +=1
    return addition_plane_need
n,m=map(int, input().split())
res=cal_req_plane(n,m)
print(res)
