class Solution:
    def removeSpaces(self, s):
        result = ""
        for ch in s:
            if ch != " ":
                result += ch
        return result
