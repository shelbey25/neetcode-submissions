class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_ids = []
        groups = {}
        
        for word in strs:
            word_id = {}
            for letter in word:
                if letter in word_id:
                    word_id[letter] += 1
                else:
                    word_id[letter] = 1
            grouping = tuple(sorted(word_id.items()))
            if grouping in groups:
                groups[grouping].append(word)
            else:
                groups[grouping] = [word]
        

        return list(groups.values())
