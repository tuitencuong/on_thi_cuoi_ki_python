
def Try(i):
    if i==n+1:
        ve.append(tmp.copy())
        return
    for j in range(1,n+1):
        if not vs[j]:
            tmp.append(j)
            vs[j]=1
            Try(i+1)
            vs[j]=0
            tmp.pop()

if __name__=='__main__':
    t=int(input())
    while t:
        t-=1
        n=int(input())
        ve=[]
        tmp=[]
        vs=[0]*(n+1)
        Try(1)
        print(len(ve))
        for i in range(len(ve)-1,-1,-1):
            for j in range(len(ve[i])):
                print(ve[i][j],end='')
            print(end=" ")
        print()
        