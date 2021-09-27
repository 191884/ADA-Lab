import time
import random
def swap(A, i, j):
	temp = A[i]
	A[i] = A[j]
	A[j] = temp


# Recursive function to perform bubble sort on sublist `A[i…n]`
def bubbleSort(A, n):
	for i in range(n - 1):
		if A[i] > A[i + 1]:
			swap(A, i, i + 1)

	if n - 1 > 1:
		bubbleSort(A, n - 1)


#Main Body
start = time.time()
n = int(input("Enter the no. of array elements: "))
A = random.sample(range(1, 999), n)
print("Given array is: ", A)
bubbleSort(A, len(A))
# print the sorted list
print("Shorted Array is: ",A)
end = time.time()
print("Time taken: ", end - start)
