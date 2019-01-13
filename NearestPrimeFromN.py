import math
def IsPrime(n):
    flag=True
    if(n==1):
        return False
    if(n==2):
        return True
    for i in range(2,int(math.sqrt(n)+1)):
        if(n%i==0):
            flag=False
            break
    return flag

def nextprime(n):
    count=0
    i=n+1
    while(count<1):
        if(IsPrime(i)):
            return i
        i+=1
def PreviousPrime(n):
    count=0
    i=n-1
    while(count<1):
        if(IsPrime(i)):
            return i
        i-=1


def NearestPrime(n):
    x=PreviousPrime(int(n))
    y=nextprime(int(n))
    y1=x-n
    y2=n-y
    if(y1<=y2):
        return x
    else:
        return y
n=input('enter the number')
print(NearestPrime(int(n)))
    
    