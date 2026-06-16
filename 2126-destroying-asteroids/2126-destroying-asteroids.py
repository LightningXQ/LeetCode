class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: list[int]) -> bool:
        ast_curr = asteroids.copy()
        ast_next = list()
        curr_mass = mass

        while True:
            for a in ast_curr:
                if curr_mass >= a: curr_mass += a
                else: ast_next.append(a)
            if not ast_next: return True
            if ast_curr == ast_next: return False
            ast_curr = ast_next
            ast_next = list()

