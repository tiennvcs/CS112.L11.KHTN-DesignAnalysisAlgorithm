import random
from doimoi import bruteforce
from improved_doimoi import binarySearch

N = 1e9
i = 1

while 1:

	try:
		a = random.randint(i, 1e9)
		b = random.randint(i, 1e9)

		k = random.randint(i+1, 1e9)
		m = random.randint(i+1, 1e9)

		n = random.randint(i+1, 1e9)
	except:
		print("Done !")

	print("a = {:8d}, k = {:8d}, b = {:8d}, m = {:8d}, n = {:8d}".format(a, k, b, m, n))

	res1 = bruteforce(a, k, b, m, n)
	res2 = binarySearch(a, k, b, m, n)

	print("Bruteforce algorithm: {}".format(res1))
	print("Improve algorithm: {}".format(res2))

	if not(res1 == res2):
		input()


