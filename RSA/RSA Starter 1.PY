'''All operations in RSA involve modular exponentiation.

Modular exponentiation is an operation that is used extensively in cryptography and is normally written like: 2^10 mod 17

You can think of this as raising some number to a certain power (2^10 = 1024), and then taking the remainder of the division by some other number (1024 mod 17 = 4). In Python there's a built-in operator for performing this operation: pow(base, exponent, modulus)

In RSA, modular exponentiation, together with the problem of prime factorisation, helps us to build a "trapdoor function". This is a function that is easy to compute in one direction, but hard to do in reverse unless you have the right information. It allows us to encrypt a message, and only the person with the key can perform the inverse operation to decrypt it.

Find the solution to 10117 mod 22663'''
print(pow(101, 17, 22663))