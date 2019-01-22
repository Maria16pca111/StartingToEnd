import math


def perfectSquare(n):
    flag=False
    for c in range(n,n*n):            
        m=math.sqrt(c)
        x=round(m)
        if(m-x==0):
            flag=True
        return flag

def kthSquare(n,k):
    if(n==1 and k==1):
        print(2)
        return

    count=0
    while(count<=k):
        if(perfectSquare(n)):
            count+=1
            if(count==k):
                print(n)
                break
        n+=1
       
        
n=input('number')
k=input('number')
kthSquare(n,k)