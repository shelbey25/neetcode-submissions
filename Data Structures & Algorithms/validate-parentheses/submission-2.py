class Solution:
    def isValid(self, s: str) -> bool:
        type1 = 0
        type2 = 0
        type3 = 0
        next_to_close_log = []

        for i in s:
            if i == '(':
                next_to_close_log.append(0)
                type1+=1
            if i == ')':
                if next_to_close_log and next_to_close_log[-1] != 0:
                    return False
                next_to_close_log = next_to_close_log[:-1]
                type1-=1
            if i == '[':
                next_to_close_log.append(1)
                type2+=1
            if i == ']':
                if next_to_close_log and next_to_close_log[-1] != 1:
                    return False
                next_to_close_log = next_to_close_log[:-1]
                type2-=1
            if i == '{':
                next_to_close_log.append(2)
                type3+=1
            if i == '}':
                if next_to_close_log and next_to_close_log[-1] != 2:
                    return False
                next_to_close_log = next_to_close_log[:-1]
                type3-=1
            if type1 < 0 or type2 < 0 or type3 < 0:
                return False
        if type1 > 0 or type2 > 0 or type3 > 0:
            return False
        return True
