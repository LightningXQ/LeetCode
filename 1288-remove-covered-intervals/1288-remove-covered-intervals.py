class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))

        result = 0
        c_intv = intervals

        while True:
            n_intv = list()

            pivot = c_intv[0]
            pr = pivot[1]
            for a in c_intv[1:]:
                ar = a[1]
                if not ar <= pr: n_intv.append(a)
            
            result += 1
            if not n_intv: break
            
            c_intv = n_intv
        
        return result
