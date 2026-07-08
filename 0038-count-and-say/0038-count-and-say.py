class Solution:
    def countAndSay(self, n: int) -> str:
        def cycle(target: str) -> str:
            result = ""

            for elm in target:
                counter = 0
                if not result or result[-1] != elm:
                    result += "1" + elm
                else:
                    result, (count, num) = result[:-2], result[-2:]
                    result += str(int(count) + 1) + num
            
            return result
        
        _in = "1"
        _out = "1"
        for _ in range(n - 1):
            _out = cycle(_in)
            _in = _out
        
        return _out