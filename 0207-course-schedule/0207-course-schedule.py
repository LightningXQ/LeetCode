class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        learned = [True] * numCourses
        courses = [set() for s in range(numCourses)]

        for i, j in prerequisites:
            courses[i].add(j)
            learned[i] = False

        class RecursionExit(Exception): pass 

        def travel(i):
            if i in visited and not learned[i]: raise RecursionExit
            visited.add(i)

            if learned[i]: 
                return True
            else:
                learned[i] = all(travel(e) for e in courses[i])

        try:
            for i in range(numCourses):
                visited = set()
                travel(i)
            return True
        except RecursionExit:
            return False
