from math import *

def test():
    n=int(input())
    a=[]
    for i in range(n):
        x,y=map(int,input().split())
        a.append([x,y])
    a.sort(key=lambda x:(x[1],x[0]))    
    cnt,end=0,0
    for key,val in a:
        if key>=end:
            cnt+=1
            end=val
    print(cnt)

if __name__=='__main__':
    t=int(input())
    while t:
        t-=1
        test()
