class Solution(object):
    def survivedRobotsHealths(self, positions, healths, directions):
        robots = []
        
        # Step 1: combine and sort
        for i in range(len(positions)):
            robots.append([positions[i], healths[i], directions[i], i])
        
        robots.sort()  # sort by position
        
        stack = []  # will store indices of robots moving right
        
        for i in range(len(robots)):
            pos, health, direction, idx = robots[i]
            
            if direction == 'R':
                stack.append(i)
            else:
                # direction == 'L'
                while stack and robots[i][1] > 0:
                    top = stack[-1]
                    
                    # if top is not R, break
                    if robots[top][2] != 'R':
                        break
                    
                    # collision
                    if robots[top][1] == robots[i][1]:
                        # both die
                        robots[top][1] = 0
                        robots[i][1] = 0
                        stack.pop()
                        break
                    elif robots[top][1] > robots[i][1]:
                        # stack robot survives
                        robots[top][1] -= 1
                        robots[i][1] = 0
                        break
                    else:
                        # current robot survives
                        robots[i][1] -= 1
                        robots[top][1] = 0
                        stack.pop()
        
        # collect survivors
        survivors = []
        for pos, health, direction, idx in robots:
            if health > 0:
                survivors.append((idx, health))
        
        # sort by original index
        survivors.sort()
        
        return [h for _, h in survivors]
        
