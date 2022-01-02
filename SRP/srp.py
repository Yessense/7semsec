import random
from sympy import isprime


def get_g(n):
    for g in range(2, 10 ** 6):
        if pow(g, int((n - 1) / 2), n) + 1 == n:
            return g


N = 2 ** 19 - 1
K = 3
G = get_g(N)


def h(*args):
    return hash(args)


class Server():
    def __init__(self, username, s, v):
        self.I = username
        self.s = s
        self.v = v

    def get_b(self, A):
        self.A = A
        if A == 0:
            raise ValueError()

        b = random.randint(1, 1000)
        self.B = (K * self.v + pow(G, b, N)) % N

        self.u = h(A, self.B)
        if self.u == 0:
            raise ValueError()

        self.S = pow(A * pow(self.v, self.u, N), b, N)
        self.K = h(self.S)
        print('Вычисление значений у сервера:')
        print(f'A: {self.A}')
        print(f'B: {self.B}')
        print(f'u: {self.u}')
        print(f'S: {self.S}')
        print(f'K: {self.K}')
        return self.B

    def verify(self, m):
        self.M = h(h(N) ^ h(G), h(self.I), self.s + self.A + self.B + self.K)
        if m != self.M:
            raise ConnectionAbortedError

        self.R = h(self.A, self.M, self.K)

        print('Вычисление значений у сервера:')
        print(f'M: {self.M}')
        print(f'R: {self.R}')
        return self.R


class Client():
    def __init__(self, username, password):
        self.username = username
        self.password = password

        self.s = random.randint(5, 20)
        self.x = h(self.s, self.password)
        self.v = pow(G, self.x, N)
        self.server = Server(self.username, self.s, self.v)
        print('Регистрация клиента:')
        print(f's: {self.s}')
        print(f'x: {self.x}')
        print(f'v: {self.v}')
        print('-' * 50)

    def login(self, password):
        print('Процедура логина:')
        print('-' * 50)
        print('Первый этап:')
        self.a = random.randint(1, 1000)
        self.A = pow(G, self.a, N)

        self.B = self.server.get_b(self.A)
        if self.B == 0:
            raise ValueError()

        self.u = h(self.A, self.B)
        if self.u == 0:
            raise ValueError()

        x = h(self.s, password)

        self.S = pow((self.B - K * pow(G, x, N)), self.a + self.u * x, N)
        self.K = h(self.S)

        print('Вычисление значений у клиента:')
        print(f'A: {self.A}')
        print(f'B: {self.B}')
        print(f'u: {self.u}')
        print(f'x: {self.x}')
        print(f'S: {self.S}')
        print(f'K: {self.K}')
        print('-' * 50)

    def verification(self):
        print('Второй этап:')
        self.M = h(h(N) ^ h(G), h(self.username), self.s + self.A + self.B + self.K)
        self.R = h(self.A, self.M, self.K)

        if self.R != self.server.verify(self.M):
            raise ConnectionAbortedError

        print('Вычисление значений у клиента:')
        print(f'M: {self.M}')
        print(f'R: {self.R}')
        print('-' * 50)
        print('Подтверждение совпало.')

    def login_and_check(self, password):
        self.login(password)
        self.verification()


if __name__ == '__main__':
    c = Client('Василий', 'Пароль')
    c.login('Yt ')
    c.verification()
