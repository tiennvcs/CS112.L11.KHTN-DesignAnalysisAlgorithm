# Input

def get_Input():
	n = int(input())  # The number of elements in array
	arr = list(map(int, input().strip().split(" ")))
	return arr


def solve(arr):
	
	p = 0
	q = 0 
	max_sum = -1e10

	l = len(arr)

	# Loop through all subarrays

	for i in range(l-1):
		for j in range(i+1, l):
			
			# Calculate the sum of elements in subarray
			current_sum = 0
			for e in range(i, j+1):
				current_sum += arr[e]

			# Update
			if current_sum > max_sum:
				p = i
				q = j
				max_sum = current_sum

	return (p, q, max_sum)

def main(arr):

	min_index, max_index, max_sum = solve(arr)
	# Display result 
	print(min_index, max_index, max_sum)

if __name__ == "__main__":
	arr = get_Input()
	main(arr)

# Test