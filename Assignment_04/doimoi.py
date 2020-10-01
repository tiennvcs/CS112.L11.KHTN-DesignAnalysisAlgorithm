def  bruteforce(a, k, b, m, n):

	number_of_tree	= 0
	day = 1

	while 1:
		if number_of_tree >= n:
			break
		if day % k != 0:
			number_of_tree += a
		if day % m != 0:
			number_of_tree += b
		#print("Ngày thứ {}: {}".format(day, number_of_tree))

		day += 1
	return day-1

if __name__ == '__main__':
	
	a, k, b, m, n = map(int, input().split())

	res = bruteforce(a, k, b, m, n)

	print(res)