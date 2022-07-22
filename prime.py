def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return print('Not prime')
        return print('prime')             
x=int(input('enter number:'))
print(test_prime(x))
