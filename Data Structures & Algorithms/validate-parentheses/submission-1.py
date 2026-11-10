class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {
        '(': ')',
        '[': ']',
        '{': '}'
        }
        stack = []
        for c in s:
            if c in "({[":
                stack.append(c)
            else:
                if len(stack) == 0:# only closing brackets case
                    return False
                d = stack.pop()
                if c != hashmap[d]:#not matching case
                    return False
        if len(stack) != 0:# this is for cases where there are only opening brackets or one open bracket dsoesnt have a close bracket
            return False
        return True
        
      

        