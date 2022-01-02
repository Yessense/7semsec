import random

primes = [19, 23, 29, 47, 59, 61, 97, 109, 113, 131, 149, 167, 179, 181, 193, 223, 229, 233, 257, 263]


def decrypt(pk, ciphertext):
    # Взять свой закрытый ключ (d, n)
    key, n = pk
    # A^b mod m
    # применить закрытый ключ для расшифрования сообщения
    plain = [chr((char ** key) % n) for char in ciphertext]
    # byte array to string
    return ''.join(plain)


def cipher(pk, plaintext):
    # Взять открытый ключ (e, n)
    key, n = pk
    # A^b mod m
    # Зашифровать сообщение с использованием открытого ключа Алисы
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
    # Выбираются два случайных простых числа p и q
    p, q = 1, 1
    while p == q:
        p = primes[random.randrange(len(primes))]
        q = primes[random.randrange(len(primes))]
    # Вычисляется их произведение, которое называется модулем
    n = p * q
    # Вычисляется значение функции Эйлера от числа n
    phi = (p - 1) * (q - 1)

    # Выбирается целое число е - взаимно простое со значением функции phi
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # Вычисляется число d, мультипликативно обратное к числу e по модулю phi
    d = i_mod(e, phi)
    public_key = (e, n)
    private_key = (d, n)
    return  public_key, private_key

if __name__ == '__main__':
    Bob_key, Alice_key = generate_keypair()

    text = 'Hello! I love you!'
    ciphered_text = cipher(Bob_key, text)
    decrypted_text = decrypt(Alice_key, ciphered_text)
    print(decrypted_text)

    print("Done")


    text = 'asdfasdf'
    # открытая экспонента и закрытая ограничения.
