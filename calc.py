"""
5/8/13
A simple program to calculate the digits of pi
inital commit
5/16/13
"""
from math import sqrt

n = int(raw_input("Enter size: ")

#inital walues

a, b, t, p = 1, 1/sqrt(2), 1/4, 1

def calc_pi(a,b,t,p,n):
    count = 0
    while count < n:
        a = an
        a = (a + b)/2
        b = sqrt(a*b)
        t = t-(p*((an-a)**2))
        p = 2*p
        count += 1
    pi = ((a+b)**2)/(4*t)
    return pi

print calc_pi(a,b,t,p,n)
    
