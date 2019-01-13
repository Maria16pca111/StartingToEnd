
def IsPrime(n):
    flag=True
    for i in range(2,n**1/2):
        if(n%i==0):
            flag=False
            break
    return flag

def prime(n):
    count=0
    
    while(count!=k):
        n+=1
        if(IsPrime(n)):
            print(n)
            count+=1
       
        
n=input('number')
k=input('number')
prime(n)