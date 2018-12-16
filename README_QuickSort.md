### QUICKSORT is my favorite SORTING ALGORITHM!!!


Like MergeSort, Quick Sort is a Devide and Conquer algorithm.
It picks an element as pivot and partitions the given array around the picked pivot.
There are many different versions of quickSort that pick pivot in different ways.
1. Always pick first element as pivot.
2. Always pick last element as pivot (implemented below)
3. Pick a random element as pivot.
4. Pick median as pivot.

The key process in quickSort is partition(). 
Target of partition is, given an array and an element x as pivot, put x at its correct position in sorted array and
put all smaller elements before x, and put all greater elements after x.
All this should be done in linear time.

```
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
```
---
```

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

```
