import itertools as it
import kanren.core as kc
from kanren import membero, run, isvar
from sympy.ntheory.generate import prime, isprime

# check if the element of x are prime
def check_prime(x):
    if isvar(x):
        return kc.condeseq([(kc.eq, x, p)] for p in map(prime, it.count(1)))
    else:
        return kc.success if isprime(x) else kc.fail

# Declare the variable
x = kc.var()

# Check if an element in the list is a prime number
list_nums = (23,4,27,17,13,10,21,29,3,11,19)
print("\nList of primes in the list:")
print(set(run(0, x, (membero, x, list_nums), (check_prime, x))))

# Print first 7 prime numbers
print("\nList of first 7 prime numbers:")
print(kc.run(7, x, check_prime(x)))