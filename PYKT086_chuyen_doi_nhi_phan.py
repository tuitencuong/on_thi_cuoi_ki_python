
def chuyen(s,k):
    cnt=1
    if k==4: cnt=2
    if k==8: cnt=3
    if k==16: cnt=4
    while len(s)%cnt!=0: s="0"+s
    ans=""
    for i in range(0,len(s),cnt):
        tmp,mu=0,1
        for j in range(cnt-1,-1,-1):
            tmp+=int(s[i+j])*mu
            mu*=2
        if(tmp>=10): ans+=chr(ord('A')+tmp-10)
        else:    ans+=str(tmp)
    return ans


if __name__=='__main__':
    with open("DATA.in",'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    T = int(lines[0])
    idx = 1
    for _ in range(T):
        k = int(lines[idx])
        s = lines[idx + 1]
        print(chuyen(s, k))
        idx += 2
        