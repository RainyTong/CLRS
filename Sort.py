# I'm a coder with good style and excellent attitude :P .

# -------------------------------------------------------------
# 1. Kth Largest Element in an Array

# Find the kth largest element in an unsorted array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element!

# O(n): QuickSelect 快速选择算法
import random


class Solution:
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


def main1():
    test_nums = [4, 6, 7, 2, 9, 1, 0, 5]
    k = 3
    solu = Solution()
    print(solu.findKthLargest(test_nums, k))


if __name__ == '__main__':
    main1()
