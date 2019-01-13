def IsPrime(n):
    flag=True
    for i in range(2,n**1/2):
        if(n%i==0):
            flag=False
            break
    return flag
def nprimes(N):
    count=0
    if(N>=1):
        print 2
        count+=1
        
        
    i=3
    while(count!=N):
        if(IsPrime(i)):
            print(i)
            count+=1
        i=i+2
        
N=input('number')
nprimes(N)


        
