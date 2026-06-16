class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: list[int]) -> bool:
        ast_curr = asteroids.copy()
        ast_prev = ast_curr.copy()
        curr_mass = mass

        while True:
            for i, a in enumerate(ast_curr):
                if curr_mass >= a:
                    curr_mass += a
                    ast_curr[i] = 0
            if not any(ast_curr): return True
            elif ast_prev == ast_curr: return False
            else: ast_prev = ast_curr.copy()

