def IsPrime(n):
    flag=True
    for i in range(2,n**1/2):
        if(n%i==0):
            flag=False
            break
    return flag

def primemton(m,n):
    count=0
    if(m==1 and m==2):
        print(2)
        count+=1
        m=3
    if(m%2==0):
        m+=1
    for i in range(m,n+1,2):
        if(IsPrime(n)):
            print(i)
            count+=1
    if(count==0):
        print 'there are 0 primeno'.format(m,n)
m=input('numberM:')
n=input('numberN:')

if(m>n):
    m,n=n,m
    
print(primemton(m,n))