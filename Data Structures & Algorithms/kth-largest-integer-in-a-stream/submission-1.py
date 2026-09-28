class KthLargest:
    def partition(self, A, start, end, k, origin_length):
        pivot = end
        index = start
        for i in range(start, end):
            if A[pivot] > A[i]:
                temp = A[index]
                A[index] = A[i]
                A[i] = temp
                index+=1
        temp = A[index]
        A[index] = A[end]
        A[end] = temp
        if origin_length-index == k-1:
            return A[index]
        if origin_length-index > k-1:
            return self.partition(A, index+1, len(A)-1, k, origin_length)
        if origin_length-index < k-1:
            return self.partition(A, start, index-1, k, origin_length)
        

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        #k_val = self.partition(nums, 0, len(nums)-1, k, len(nums)-1)
        


    def add(self, val: int) -> int:
        self.nums.append(val)
        k_val = self.partition(self.nums, 0, len(self.nums)-1, self.k, len(self.nums)-1)
        return k_val
        
