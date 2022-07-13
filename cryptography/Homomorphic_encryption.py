import math
from random import randint

nkeys = 100  # размер массива публичных ключей
PublicKey = [0] * nkeys  # массив публичных ключей
PrivateKey = 0  # секретный ключ
b1 = 10 ** 20  # нижняя граница диапазона значений ключей
b2 = b1 ** 2  # верхняя граница диапазона значений ключей
modulo = b1  # порядок группы


def gcd(a, b):               # вычисление НОД(а,b)
    return math.gcd(a, b)


def keygen():  # функция генерации ключей
    global nkeys, PublicKey, PrivateKey, modulo, b1, b2
    while True:
        PrivateKey = randint(b1, b2)
        if gcd(PrivateKey, modulo) == 1:
            break
    PublicKey = [(randint(b1, b2) * PrivateKey) + (modulo * randint(10, 100)) for i in range(0, nkeys)]
    return PublicKey, PrivateKey


result = keygen()
pk = result[0]
sk = result[1]
message = 77888555434598765
print("Message:", message)


def Encrypt(m):
    global nkeys, pk
    return m+sum([PublicKey[i] for i in range(0, nkeys) if randint(0, 1) == 1])


encrypted = Encrypt(message)
print('Encrypted message:', encrypted)


def Decrypt(c):
    global sk, modulo
    return (c % PrivateKey) % modulo


print('Decrypted message:', Decrypt(encrypted))
