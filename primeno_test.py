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
def test_isprime_between_mton():
    assert isprime_between_mton(25,50)

def isprime_between_mton(m,n):
    return True

def test_print_prime_factors():
    assert isprime_factors(40)

def isprime_factors(n):
    return True
#code

import math
def isprimee(n):
    flag=False
    for x in range(0,n+1):
        if(x%n==0):
            flag=True
    return flag

# code
def isprime_upto_nth_noo(n):
    flag=False
    for x in range(0,n+1):
        if(x%n==0):
            flag=True
        else:
            print(x)
    return flag

#code
def IsPrime(n):
    flag=True
    for i in range(2,n**1/2):
        if(n%i==0):
            flag=False
            break
    return flag

def isprime_found_kth_no_from_n(n,k):
    if(n==1 or k==1):
        print(2)
        return
    
    count=0
    while(count<=k):
        if(isprime(n)):
            count+=1 
            if(count==k):
                print(n)
                break
        n+=1     
isprime_found_kth_no_from_n(20,5)

def isprime_count_upto_nth_noo(n):
    flag=False
    count=0    
    if(IsPrime(n)):
        flag=True
        count+=1
        print'total count is',count
    return flag
isprime_count_upto_nth_no(20)


#code
def isprime_between_mton1(m,n):
 for num in range(m,n + 1):
 
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
isprime_between_mton(25,50)

#code
def isprime_factorss(n):
    Flag=False
    for x in range(1,n+1):
        if(x%n==0):
            Flag=True
            print(x)
    return Flag
isprime_factors(40)



    


    


