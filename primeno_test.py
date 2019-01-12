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
def isprime_count_upto_nth_noo(n):
    flag=False
    count=0
    if(n>0):
        print(2)
        count+=1
        
    for x in range(3,math.sqrt(n+1),2):
        if(x%n==0):
            break
        else:
            count+=1
        print(count)
    return flag
    


    


