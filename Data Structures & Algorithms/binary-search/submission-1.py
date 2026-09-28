class Solution:
    def binary_search(self, nums, start, end, target):
        pivot = start+(end-start)//2
        if nums[pivot] == target:
            return start+(end-start)//2
        elif end-start <= 1:
            return -1
        elif nums[pivot] < target:
            return self.binary_search(nums, pivot, end, target)
        elif nums[pivot] > target:
            return self.binary_search(nums, start, pivot, target)

    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, 0, len(nums), target)
        