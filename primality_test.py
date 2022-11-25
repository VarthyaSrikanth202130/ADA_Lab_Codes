"""Q. Program to implement Primality Test using Fermat Method"""

import random
def fast_exp(a, e, m):              #iterative function to calculate (a**e)%m
    r = 1
    if 1 & e:
        r = a
    while e:
        e >>= 1
        a = (a * a) % m
        if e & 1: r = (r * a) % m
    return r

def fermat_test(n):                 #function to check wether prime or not
    n=int(n)
    a=random.randint(2,n-2)
    r=fast_exp(a,(n-1),n)
    if r == 1:
        return True
    else:
        return False
#main Code
def test():
    number = int(input("Enter the number for primality test: "))
    if fermat_test(number) == True:
        print("Probably Prime")
    else:
        print("Probably not a Prime")
test()