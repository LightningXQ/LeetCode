class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)
        result = 0

        for i in range(n):
            c = s[i]
            if i > 0: p_c = s[i - 1]
            else: p_c = None

            match c:
                case "M":
                    if p_c == "C":
                        result += 800
                    else: result += 1000
                case "D":
                    if p_c == "C":
                        result += 300
                    else: result += 500
                case "C": 
                    if p_c == "X":
                        result += 80
                    else: result += 100
                case "L":
                    if p_c == "X":
                        result += 30
                    else: result += 50
                case "X":
                    if p_c == "I":
                        result += 8
                    else: result += 10
                case "V":
                    if p_c == "I":
                        result += 3
                    else: result += 5
                case "I": result += 1
        
        return result