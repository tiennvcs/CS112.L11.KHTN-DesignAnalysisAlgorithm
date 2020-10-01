import math

def binarySearch(a, k, b, m, n):

	def f(t: int):

		return (a+b)*t - (int(t//k)*a+int(t//m)*b)


	low = 1
	high = n

	while low <= high:

		#print("Low: {} --> High: {}".format(low, high))
		mid = int((low + high) // 2)

		value = f(t=mid)
		#print("The middle value: {}".format(value))

		if value == n:
			return mid

		if value < n:
			low = mid + 1
		else:
			high = mid - 1

	return low


if __name__ == "__main__":
	
	a, k, b, m, n = map(int, input().split())

	res = binarySearch(a, k, b, m, n)

	print(res)


