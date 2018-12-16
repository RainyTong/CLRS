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



# -------------------------------------------------------------
# O(n^2): Selection Sort, Insertion Sort, Bubble Sort


