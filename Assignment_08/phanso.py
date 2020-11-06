import math
import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
d = int(sys.stdin.readline())

number_of_steps = 0

if (a - b < c - d) and (a == b or c == d):
    sys.stdout.write('0')
    system.exit(0)

number_of_steps = 0
while not (a == c and b == d):
    a += 1
    b += 1
    ucln = math.gcd(a, b)
    a //= ucln
    b //= ucln
    number_of_steps += 1
    if (number_of_steps == 200000):
        break
if number_of_steps < 200000:
    sys.stdout.write(str(number_of_steps))
else:
    sys.stdout.write('0')
