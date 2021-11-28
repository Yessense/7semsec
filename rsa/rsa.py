import random

primes = [19, 23, 29, 47, 59, 61, 97, 109, 113, 131, 149, 167, 179, 181, 193, 223, 229, 233, 257, 263]


def decrypt(pk, ciphertext):
    key, n = pk
    # a^b mod m
    plain = [chr((char ** key) % n) for char in ciphertext]
    # byte array to string
    return ''.join(plain)


def cipher(pk, plaintext):
    key, n = pk
    # a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]
    # byte array
    return cipher


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def i_mod(a, n):
    c = 1
    while c % a > 0:
        c += n
    return c // a


def num_of_rel_primes(p):
    i = 0
    for each in range(1, p):
        if gcd(each, p) == 1:
            i += 1
    return i


def generate_keypair():
    p, q = 1, 1
    while p == q:
        p = primes[random.randrange(len(primes))]
        q = primes[random.randrange(len(primes))]
    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    d = i_mod(e, phi)
    return (e, n), (d, n)
