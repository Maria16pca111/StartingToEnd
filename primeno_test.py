#working up test cases for primeno variants

def test_prime_is_prime_or_not():
    assert isprime(7)

def isprime(n):
    return True

def test_prime_is_not():
    assert isprime_is_not(25)

def isprime_is_not(n):
    return True

def test_isprime_upto_n():
    assert isprime_upto_nth_no(15)

def isprime_upto_nth_no(n):
    return True

def test_isprime_count_upto_n():
    assert isprime_count_upto_nth_no(25)

def isprime_count_upto_nth_no(n):
    return True

def test_isprime_found_kth_no_from_n():
    assert isprime_kth_no_from_n(25)

def isprime_kth_no_from_n(n):
    return True

    
#code

import math
def isprimee(n):
    flag=False
    for x in range(0,n+1):
        if(x%n==0):
            flag=True
    return flag

#refactoring code
def isprime_upto_nth_noo(n):
    flag=False
    for x in range(0,n+1):
        if(x%n==0):
            flag=True
        else:
            print(x)
    return flag

#refactoring code
def IsPrime(n):
    flag=True
    for i in range(2,n**1/2):
        if(n%i==0):
            flag=False
            break
    return flag


#refactoring code
# def nprimes(N):
#     count=0
#     if(N>=1):
#         print 2
#         count+=1      
        
#     i=3
#     while(count!=N):
#         if(IsPrime(i)):
#             print(i)
#             count+=1
#         i=i+2
        
# N=input('number')
# nprimes(N)
    


    


