# I'm a coder with good style and excellent attitude :P .

# -------------------------------------------------------------
# 1. Kth Largest Element in an Array

# Find the kth largest element in an unsorted array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element!


import random


# -------------------------------------------------------------
# O(n): QuickSelect 快速选择算法
class QuickSelect:

    def findKthLargest(self, nums, k):
        pivot = random.choice(nums)
        nums1 = []
        nums2 = []
        for num in nums:
            if num > pivot:
                nums1.append(num)
            elif num < pivot:
                nums2.append(num)
        if len(nums1) >= k:
            return self.findKthLargest(nums1, k)
        if (len(nums) - len(nums2)) < k:
            return self.findKthLargest(nums2, k - (len(nums) - len(nums2)))
        return pivot


# -------------------------------------------------------------
# O(n log n): HeapSort, MergeSort, DevideAndConquerSort
class DevideAndConquerSort:

    def de_and_conq_Sort(self, nums):
        less = []
        equal = []
        greater = []
        if len(nums) > 1:
            pivot = random.choice(nums)
            for num in nums:
                if num < pivot:
                    less.append(num)
                if num == pivot:
                    equal.append(num)
                if num > pivot:
                    greater.append(num)
            # Don't forget to return something!
            return self.de_and_conq_Sort(less) + equal + self.de_and_conq_Sort(greater)
        else:
            return nums

    def findKthLargest(self, nums, k):
        ord_nums = self.de_and_conq_Sort(nums)
        rev_ord_nums = ord_nums[::-1]
        return rev_ord_nums[k-1]

# -------------------------------------------------------------
# avg ==> O(n log n), wst ==> O(n^2): Quick Sort

# Like MergeSort, Quick Sort is a Devide and Conquer algorithm.
# It picks an element as pivot and partitions the given array around the picked pivot.
# There are many different versions of quickSort that pick pivot in different ways.
# 1. Always pick first element as pivot.
# 2. Always pick last element as pivot (implemented below)
# 3. Pick a random element as pivot.
# 4. Pick median as pivot.

# The key process in quickSort is partition(). Target of partition is, given an array and
# an element x as pivot, put x at its correct position in sorted array and
# put all smaller elements before x, and put all greater elements after x.
# all this should be done in linear time.

class QuickSort:

    def partition(self, array, left, right):
        i = left - 1  # i points to the last "smaller than pivot" element
        for j in range(left, right):
            if array[j] <= array[right]:
                i = i + 1
                array[j], array[i] = array[i], array[j]
        array[i+1], array[right] = array[right], array[i+1]
        return i+1

    def quicksort(self, array, left, right):
        if left < right:
            p = self.partition(array, left, right)
            self.quicksort(array, left, p-1)
            self.quicksort(array, p+1, right)

# Test:
# Q = QuickSort()
# array = [3, 2, 1, 0, 9, 8, 7, 6, 5, 4]
# Q.quicksort(array, 0, len(array)-1)
# print(array)


# -------------------------------------------------------------
# O(n^2): Selection Sort, Insertion Sort, Bubble Sort


