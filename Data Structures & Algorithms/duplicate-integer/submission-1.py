class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sorted = self.merge_sort(nums)
        for i in range(1, len(sorted)):
            if sorted[i] == sorted[i-1]:
                return True
        return False

    def merge_sort(self, a):
        if (len(a) == 1 or len(a) == 0):
            return a

        l = a[:len(a)//2]
        r = a[len(a)//2:]

        l = self.merge_sort(l)
        r = self.merge_sort(r)
        
        combined = []

        l1 = 0
        r1 = 0

        while (l1 < len(l) or r1 < len(r)):
            if l1 == len(l):
                combined.append(r[r1])
                r1 += 1
                continue
            if r1 == len(r):
                combined.append(l[l1])
                l1 += 1
                continue

            if l[l1] < r[r1]:
                combined.append(l[l1])
                l1 += 1
            else:
                combined.append(r[r1])
                r1 += 1

        return combined

        