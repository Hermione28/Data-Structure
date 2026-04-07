class Solution:
    def stableMarriage(self, men, women):
        n = len(men)
        
        # महिला की preference ranking (fast comparison के लिए)
        rank = [[0]*n for _ in range(n)]
        for w in range(n):
            for i in range(n):
                rank[w][women[w][i]] = i
        
        # कौन engaged है
        women_partner = [-1]*n
        men_partner = [-1]*n
        
        # हर आदमी का next proposal index
        next_proposal = [0]*n
        
        free_men = list(range(n))
        
        while free_men:
            m = free_men.pop(0)
            w = men[m][next_proposal[m]]
            next_proposal[m] += 1
            
            # अगर महिला free है
            if women_partner[w] == -1:
                women_partner[w] = m
                men_partner[m] = w
            else:
                current = women_partner[w]
                
                # महिला compare करेगी
                if rank[w][m] < rank[w][current]:
                    women_partner[w] = m
                    men_partner[m] = w
                    men_partner[current] = -1
                    free_men.append(current)
                else:
                    free_men.append(m)
        
        return men_partner
