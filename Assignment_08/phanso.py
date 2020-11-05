import math

a = int(input())
b = int(input())
c = int(input())
d = int(input())

number_of_steps = 0

while not (a == c and b == d):
    a += 1
    b += 1
    ucln = math.gcd(a, b)
    a //= ucln
    b //= ucln
    number_of_steps += 1

print(number_of_steps)
