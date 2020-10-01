
def find_H_index(arr: list):
	n = len(arr)
	arr = sorted(arr)
	for i in range(n):
		current_result = n - i
		if current_result <= arr[i]:
			return current_result
	return 0

if __name__ == '__main__':
	n = int(input())
	arr = list(map(int, input().split()))
	result = find_H_index(arr)
	print(result)