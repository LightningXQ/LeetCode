class Solution:
    def simplifyPath(self, path: str) -> str:
        pathes = path.split("/")
        result = list()

        for p in pathes:
            if p and p != ".":
                if p == "..":
                    if not result: continue
                    result.pop()
                else:
                    result.append(p)
        
        return "/" + "/".join(result)
