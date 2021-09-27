# Recursive function to perform insertion sort on sublist `A[i…n]`
import time
import random
import sys
def insertionSort(A, i, n):
	value = A[i]
	j = i

	# find index `j` within the sorted subset `A[0…i-1]`
	# where element `A[i]` belongs
	while j > 0 and A[j - 1] > value:
		A[j] = A[j - 1]
		j = j - 1

	A[j] = value

	# Note that sublist `A[j…i-1]`is shifted to
	# the right by one position, i.e., `A[j+1…i]`

	if i + 1 <= n:
		insertionSort(A, i + 1, n)

#Main Body
sys.setrecursionlimit(3001)
start = time.time()
n = int(input("Enter the no. of array elements"))
A = random.sample(range(1, 999), n)
# start from the second element (the element at index 0 is already sorted)
insertionSort(A, 1, len(A) - 1)
# print the sorted list
print(A)
end = time.time()
print("Time taken: ", end - start)
