# python program for checking is prime number or not

import math

def prime(arg):
    if arg <= 1 :
        return False
    if arg == 2 :
        return True
    max_of = math.ceil(math.sqrt(arg))
    if arg > 2 :
        for i in range (3 , 1+ max_of):
            if arg % i == 0:

                return False
        return True
prime_func  = prime(22)
if prime_func == True:
    print("prime")
else:
    print("not prime")