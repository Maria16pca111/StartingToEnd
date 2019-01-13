def IsPrime(n):
    flag=True
    for i in range(2,n**1/2):
        if(n%i==0):
            flag=False
            break
    return flag


def primesprint(N):
    if(N>=2):
        print(2)
        
        for i in range(3,N+1,2):
            if(IsPrime(i)):
                print(i)
                
N=input('number')
primesprint(N)