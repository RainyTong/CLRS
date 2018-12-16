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


class RandomQuickSort:

    def partition(self, nums, left, right):
        p = random.randint(left, right)
        pivot = nums[p]
        nums_copy = nums[:]
        for i in range(left, right+1):
            if i == p:
                continue
            num = nums[i]
            if num <= pivot:
                nums_copy[left] = num
                left += 1
            if num > pivot:
                nums_copy[right] = num
                right -= 1
        nums_copy[left] = pivot
        return left, nums_copy

    def quicksort(self, nums, left, right):
        if left < right:
            p, nums = self.partition(nums, left, right)
            nums = self.quicksort(nums, left, p-1)
            nums = self.quicksort(nums, p+1, right)
        return nums


# -------------------------------------------------------------
# O(n^2): Selection Sort, Insertion Sort, Bubble Sort


