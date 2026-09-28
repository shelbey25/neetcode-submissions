class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mega_word = ""
        index = 0
        while len(mega_word) < len(word1) + len(word2):
            if index%2 == 0:
                if index//2 < len(word1):
                    mega_word += word1[index//2]
            else: 
                if index//2 < len(word2):
                    mega_word += word2[index//2]
            index+=1
        return mega_word