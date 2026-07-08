class Solution:
    def countAndSay(self, n: int) -> str:
        def cycle(target: str) -> str:
            result = ""
            prev = ""
            counter = 0

            for elm in target:
                if prev == "":
                    prev = elm
                    counter += 1
                    continue
                
                if elm == prev:
                    counter += 1
                else:
                    result += str(counter) + prev
                    prev = elm 
                    counter = 1
            
            result += str(counter) + prev
            
            return result
        
        _in = "1"
        _out = "1"
        for _ in range(n - 1):
            _out = cycle(_in)
            _in = _out
        
        return _out