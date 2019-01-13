def IsPrime(n):
    flag=True
    for i in range(2,n**1/2):
        if(n%i==0):
            flag=False
            break
    return flag

def kthprime(n,k):
    if(n==1 and k==1):
        print(2)
        return

    count=0
    while(count<=k):
        if(IsPrime(n)):
            count+=1
            if(count==k):
                print(n)
                break
        n+=1
       
        
n=input('number')
k=input('number')
kthprime(n,k)
    