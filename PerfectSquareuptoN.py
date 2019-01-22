import math
def perfectSquare(n):
    flag=False
    m=math.sqrt(n)
    x=round(m)
    if(m-x==0):
        flag=True
    return flag

def perfectsquareupton(n):
    flag=False
    for x in range(0,n+1):
        if(perfectSquare(x)):
            flag=True
            print(x)
    return flag
perfectsquareupton(40)
