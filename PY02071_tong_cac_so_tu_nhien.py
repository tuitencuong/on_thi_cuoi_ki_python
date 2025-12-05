from math import *

def Try(i,sum):
    if sum==n: 
        ve.append(tmp.copy())
        return
    for j in range(1,n+1):
        if(sum+j<=n):
            if len(tmp)==0 or j<=tmp[len(tmp)-1]:
                tmp.append(j)
                Try(i+1,sum+j)
                tmp.pop()
if __name__=='__main__':
    t=int(input())
    while t:
        n=int(input())
        ve=[]
        tmp=[]
        Try(1,0)
        t-=1
        print(len(ve))
        for i in range(len(ve)-1,-1,-1):
            print(end='(')
            for j in range(len(ve[i])):
                print(ve[i][j],end='')
                if j!=len(ve[i])-1: print(end=" ")
            print(end=') ')
        print()
