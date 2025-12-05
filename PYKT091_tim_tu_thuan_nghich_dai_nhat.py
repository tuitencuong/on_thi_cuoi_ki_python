if __name__=='__main__':
    d={}
    max1=0
    with open('VANBAN.in','r') as f:
        for line in f:
            line = line.strip()
            if line:
                tmp=list(line.split())
                for x in tmp:
                    if x==x[::-1]:
                        max1=max(max1,len(x))
                        if x in d:
                            d[x]+=1
                        else: d[x]=1
    for key,val in d.items():
        if len(key)==max1:
            print(key,val)
