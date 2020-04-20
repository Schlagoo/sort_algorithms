""" Implementation of different sorting algorithms in Python3 including: 
	InsertionSort, SelectionSort, BubbleSort, MergeSort, QuickSort.

	Author:		https://github.com/Schlagoo
	Date:		2020/04/20 		
	Python: 	3.6.9
"""


class SortingAlgorithms:

	def __init__(self, arr: list):
		self.arr = arr

	def insertion_sort(self) -> list:
    
		""" Insertion sort list by iterting through list and checking if previous element is bigger.

		:return		self.arr	Sorted list
		"""

		for i in range(1, len(self.arr)):
			
			j = i
			marker = self.arr[i]

			while (j > 0 and self.arr[j - 1] > marker):

				self.arr[j] = self.arr[j - 1]
				j -= 1
				
			self.arr[j] = marker

		return self.arr

	def selection_sort(self) -> list:
    
		""" Selection sort list by searching for max element and put in at the end of list.
		
		:return		self.arr	Sorted list
		"""

		n = len(self.arr) - 1

		while n >= 0:

			max = 0

			for i in range(1, n + 1):
				if self.arr[i] > self.arr[max]:
					max = i

			self.arr[n], self.arr[max] = self.arr[max], self.arr[n]
			n -= 1

		return self.arr

	def bubble_sort(self) -> list:

		""" Bubble sort algorithm to sort list by iterating through list and comparing values of i and i+1

		:return		self.arr	Sorted list
		"""

		for _ in range(len(self.arr)):
			for i in range(len(self.arr) - 1):
				if self.arr[i] > self.arr[i + 1]:
					self.arr[i], self.arr[i + 1] = self.arr[i + 1], self.arr[i]
		
		return self.arr

	def merge_sort(self, arr: list) -> list:

		""" Merge sort algorithm to sort list elements by size.

		:param		arr			List containing elements
		:return		merge()		Function to merge subsets 	
		"""

		if len(arr) < 2:
			return arr

		left_half, right_half = [], []
		m = len(arr) // 2

		left_half = self.merge_sort(arr[:m])
		right_half = self.merge_sort(arr[m:])

		return self.merge(left_half, right_half)


	def merge(self, left_half: list, right_half: list) -> list:

		""" Merge left and right half of list by sorting elements.

		:param		left_half	Left subset of elements
		:param		right_half	Right subset of elements
		:return		merger 		Result of merging left and right half
		"""

		merger = []
		i, j = 0, 0

		while (len(merger) < len(left_half) + len(right_half)):
			
			if left_half[i] < right_half[j]:
				merger.append(left_half[i])
				i+= 1
			else:
				merger.append(right_half[j])
				j+= 1

			if i == len(left_half) or j == len(right_half):
				merger.extend(left_half[i:] or right_half[j:])

		return merger

	def quick_sort(self, arr: list, lower: int, upper: int) -> list:    

		""" Quick sort list by generating pivot element, partition and sort subsets.
		
		:param		arr			List containing elements
		:param		lower		Lower bound of current subset
		:param		upper		Upper bound of current subset
		:return		arr			Sorted list
		"""

		if upper > lower:
			pivot = (lower + upper) // 2
			new_pivot = self.sort_partitions(arr, lower, upper, pivot)
			arr = self.quick_sort(arr, lower, new_pivot - 1)
			arr = self.quick_sort(arr, new_pivot + 1, upper)

		return arr


	def sort_partitions(self, arr: list, lower: int, upper: int, pivot: int) -> int:

		""" Sort partitions of elements.
		
		:param		arr			List containing elements
		:param		lower		Lower bound of current subset
		:param		upper		Upper bound of current subset
		:param		pivot		Current pivot element
		:return		new_pivot	Next pivot element
		"""

		new_pivot = lower
		value_pivot = arr[pivot]
		
		arr[pivot], arr[upper] = arr[upper], arr[pivot]
		
		for i in range(lower, upper):
			if arr[i] <= value_pivot:
				arr[new_pivot], arr[i] = arr[i], arr[new_pivot]
				new_pivot += 1
		
		arr[new_pivot], arr[upper] = arr[upper], arr[new_pivot]
		
		return new_pivot


if __name__ == "__main__":
	a = SortingAlgorithms([5, 3, 1, 7, 4, 6])
	# print("Insertion sorted list: {}".format(a.insertion_sort()))
	# print("Selection sorted list: {}".format(a.selection_sort()))
	# print("Bubble sorted list: {}".format(a.bubble_sort()))
	# print("Merge sorted list: {}".format(a.merge_sort([5, 3, 1, 7, 4, 6])))
	print("Quick sorted list: {}".format(a.quick_sort([5, 3, 1, 7, 4, 6], lower=0, upper=5)))
