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
n=input('number')
print(nextprime(int(n)))
nextprime(n)
    
    