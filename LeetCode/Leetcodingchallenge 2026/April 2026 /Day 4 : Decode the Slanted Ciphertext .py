class Solution(object):
    def decodeCiphertext(self, encodedText, rows):
        if rows == 1:
            return encodedText
        
        n = len(encodedText)
        cols = n // rows
        
        
        matrix = []
        idx = 0
        for r in range(rows):
            matrix.append(list(encodedText[idx:idx+cols]))
            idx += cols
        
        
        result = []
        
        for start_col in range(cols):
            r, c = 0, start_col
            
            while r < rows and c < cols:
                result.append(matrix[r][c])
                r += 1
                c += 1
        
        
        return "".join(result).rstrip()
