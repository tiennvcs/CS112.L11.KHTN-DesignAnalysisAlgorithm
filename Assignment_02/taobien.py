def fibonacy(k: int):
	if k == 0 or k == 1:
		return 1

	a = 1
	b = 1
	for i in range(2, k+1):
		a, b = b, a + b

	return b

n, k = map(int, input().split())

result = n*fibonacy(2*k)
print(result%(10^9+7))