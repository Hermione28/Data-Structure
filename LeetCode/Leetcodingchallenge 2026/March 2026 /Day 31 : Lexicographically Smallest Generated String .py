class Solution(object):
    def generateString(self, str1, str2):
        n, m = len(str1), len(str2)
        word = ['?'] * (n + m - 1)

        # Step 1: Apply 'T'
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    if word[i + j] == '?' or word[i + j] == str2[j]:
                        word[i + j] = str2[j]
                    else:
                        return ""

        # Step 2: Mark locked positions
        locked = [False] * (n + m - 1)
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    locked[i + j] = True

        # Step 3: Fill remaining '?'
        for i in range(len(word)):
            if word[i] == '?':
                word[i] = 'a'

        # Step 4: Fix 'F'
        for i in range(n):
            if str1[i] == 'F':
                if "".join(word[i:i+m]) == str2:
                    changed = False

                    for j in range(m-1, -1, -1):
                        idx = i + j
                        
                        if locked[idx]:
                            continue  # cannot change

                        original = word[idx]
                        
                        for c in ['a', 'b']:
                            if c != original:
                                word[idx] = c
                                if "".join(word[i:i+m]) != str2:
                                    changed = True
                                    break
                                word[idx] = original
                        
                        if changed:
                            break

                    if not changed:
                        return ""

        return "".join(word)
