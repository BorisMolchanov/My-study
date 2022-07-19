from random import randint

m = 2022  # the message
p = 277  # prime number
g = [x for x in range(1, p) if len(set([x ** i % p for i in range(1, p)])) == p - 1][0]
r = randint(1, p - 1)
h = g ** r % p
c = ((g ** m) * (h ** r)) % p  # Pedersen commitment
check = (g ** m * h ** r) % p

print('The message is:', m)
print("It works!") if check == c else print("Try again!")
