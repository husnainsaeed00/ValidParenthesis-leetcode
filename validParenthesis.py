class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
            elif char in [')', '}', ']']:
                if not stack:
                    return False
                opening_bracket = stack.pop()
                if (char == ')' and opening_bracket != '(') or \
                   (char == '}' and opening_bracket != '{') or \
                   (char == ']' and opening_bracket != '['):
                    return False
        return not stack
