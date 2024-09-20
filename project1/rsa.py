import random
import sys

# This may come in handy...
from fermat import miller_rabin

# If you use a recursive implementation of `mod_exp` or extended-euclid,
# you recurse once for every bit in the number.
# If your number is more than 1000 bits, you'll exceed python's recursion limit.
# Here we raise the limit so the tests can run without any issue.
# Can you implement `mod_exp` and extended-euclid without recursion?
sys.setrecursionlimit(4000)

# When trying to find a relatively prime e for (p-1) * (q-1)
# use this list of 25 primes
# If none of these work, throw an exception (and let the instructors know!)
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


# Implement this function
def ext_euclid(a: int, b: int) -> tuple[int, int, int]:
    if b == 0: 
        return a, 0, 1
    else:
        x, y, d = ext_euclid(b, a % b)
    return y, (x - ((a//b)*y)), d


# Implement this function
def generate_large_prime(bits=512) -> int:
    x = random.getrandbits(bits)
    while miller_rabin(x, 20) != "prime":
        x = random.getrandbits(bits)
    return x


# Implement this function
def generate_key_pairs(bits: int) -> tuple[int, int, int]:
    p = generate_large_prime(bits)
    q = generate_large_prime(bits)
    N = p*q
    relativeN = (p-1)*(q-1)
    
    for testprime in primes:
        if  relativeN % testprime != 0:
            e = testprime
            break 

    d = ext_euclid(relativeN, e)[1]
    if d < 0:
        d = d + relativeN

    return N, e, d
