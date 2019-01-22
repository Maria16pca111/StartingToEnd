#given no is perfect Square or not
import math
def perfectSquare(n):
    flag=False
    m=math.sqrt(n)
    x=round(m)
    if(m-x==0):
        flag=True
    return flag
print perfectSquare(35)
