class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        result = sorted(freq, key=freq.get, reverse=True)
            
        return result[:k]
"""
    def merge_sort(self, a):
        if len(a) == 1 or len(a) == 0:
            return a
        
        l = a[len(a)//2:]
        r = a[:len(a)//2]

        l = self.merge_sort(l)
        r = self.merge_sort(r)

        return self.merge(l, r)

    def merge(self, l, r):
        combined = []
        l1 = 0
        r1 = 0

        while (l1 < len(l)) or (r1 < len(r)):
            if (r1 == len(r)):
                combined.append(l[l1])
                l1+=1
            elif (l1 == len(l) or r[r1] < l[l1]):
                combined.append(r[r1])
                r1+=1
            else: 
                combined.append(l[l1])
                l1+=1
        
        return combined
"""
        


