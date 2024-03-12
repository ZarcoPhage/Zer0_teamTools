'''
RSA relies on the difficulty of the factorisation of the modulus N. 
If the primes can be found then we can calculate the Euler totient of N and thus decrypt the ciphertext.

Given N = p*q and two primes:

p = 857504083339712752489993810777

q = 1029224947942998075080348647219

What is the totient of N?'''
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = egcd(b % a, a)
        return gcd, y - (b // a) * x, x
from functools import reduce
def chinese_remainder(m, a):
    sum = 0
    prod = reduce(lambda acc, b: acc*b, m)
    for n_i, a_i in zip(m, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1
 

p = 857504083339712752489993810777

q = 1029224947942998075080348647219
phi = (p-1)*(q-1)
# Inversa de N, o Totient
print(phi)