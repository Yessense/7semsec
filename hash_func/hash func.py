def hash_func(string, seed=0):
    big_prime = 2 ** 19 - 1
    salt = 146959

    hash = salt + seed
    for char in string:
        hash = hash ^ ord(char)
        hash = hash * big_prime
    return hash


if __name__ == '__main__':
    s = 'Он открыл дверь и увидел меня'
    h = hash_func(s, 1)
    print(h)

    s = 'Он открыл дверь и увидел меня'
    h = hash_func(s, 0)
    print(h)

    s = 'Мы катались на аттракционах'
    h = hash_func(s, 2)
    print(h)
