# python program for checking is prime number or not

import math

#make fuction for checking numbers
def prime(arg):
    if arg <= 1 :
        return False
    if arg == 2 :
        return True
    if arg % 2 == 0 :
        return False
    max_of = math.ceil(math.sqrt(arg))
    if arg > 2 :
        for i in range (3 , 1+ max_of):
            if arg % i == 0:
                return False
        return True


while True:                          #to dont stop loop
    number = int(input())            #resived number from input 
    prime_func  = prime(number)      #get fuction
    if prime_func == True:           #printing function result
        print("prime")
    else:
        print("not prime")