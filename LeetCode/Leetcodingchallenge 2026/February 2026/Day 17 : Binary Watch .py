class Solution(object):
    def readBinaryWatch(self, turnedOn):
        result = []
        
        for hour in range(12):        # 0–11
            for minute in range(60):  # 0–59
                
                # Count LEDs ON
                if bin(hour).count('1') + bin(minute).count('1') == turnedOn:
                    
                    # Format minute with leading zero
                    time_str = "{}:{:02d}".format(hour, minute)
                    result.append(time_str)
        
        return result

        
        return result

