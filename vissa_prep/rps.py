ch,vi=map(str,input().split())
if(ch=='R' and vi=='P') or (ch=='S' and vi=='R') or (ch=='P' and vi=='S'):
    print("Charan")
elif(ch=='P' and vi=='R') or (ch=='R' and vi=='S') or (ch=='S' and vi=='P'):
    print("Vignesh")
else:
    print("NULL")
