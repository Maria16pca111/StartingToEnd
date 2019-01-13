count=0
n=0
n=int(input('number'))
for num in range(2,n+1):
    if(num>1):
        for i in range(2,num):
            if(num % i) == 0:
                break
        else:
            print(num)
            n += 1
            count += 1
print('total count is',count)         