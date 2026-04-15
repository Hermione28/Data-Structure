class Solution:
    def URLify(self, s): 
        # count spaces
        spaces = s.count(' ')
        
        # if no spaces, return original
        if spaces == 0:
            return s
        
        # convert string to list for mutability
        s = list(s)
        len_original = len(s)
        new_len = len_original + 2 * spaces
        
        # resize list
        s.extend([''] * (2 * spaces))
        
        i = len_original - 1
        j = new_len - 1
        
        # fill from end
        while i >= 0:
            if s[i] == ' ':
                s[j] = '0'
                s[j-1] = '2'
                s[j-2] = '%'
                j -= 3
            else:
                s[j] = s[i]
                j -= 1
            i -= 1
        
        return ''.join(s)
        
