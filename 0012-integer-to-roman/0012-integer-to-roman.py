class Solution:
    def intToRoman(self, num: int) -> str:
        result = list()

        while num >= 1000:
            num -= 1000
            result.append("M")
        
        if num >= 900:
            num -= 900
            result.append("CM")
        else:
            while num >= 500:
                num -= 500
                result.append("D")
        
        if num >= 400:
            num -= 400
            result.append("CD")
        else:
            while num >= 100:
                num -= 100
                result.append("C")
        
        if num >= 90:
            num -= 90
            result.append("XC")
        else:
            while num >= 50:
                num -= 50
                result.append("L")
        
        if num >= 40:
            num -= 40
            result.append("XL")
        else:
            while num >= 10:
                num -= 10
                result.append("X")
        
        if num >= 9:
            num -= 9
            result.append("IX")
        else:
            while num >= 5:
                num -= 5
                result.append("V")
        
        if num >= 4:
            num -= 4
            result.append("IV")
        else:
            while num >= 1:
                num -= 1
                result.append("I")
            
        return "".join(result)