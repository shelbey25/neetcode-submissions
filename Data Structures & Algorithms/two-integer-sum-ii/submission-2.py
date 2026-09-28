class Solution:
    def partition(self, A, start, end, target):
        pivot = (start+end)//2
        if A[pivot] == target:
            return pivot
        if end - start <= 1:
            return None

        if A[pivot] > target:
            return self.partition(A, start, pivot, target)
        else:
            return self.partition(A, pivot, end, target)
    
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            val = self.partition(numbers, i+1, len(numbers), target-numbers[i])
            if val: 
                return [i+1, val+1]