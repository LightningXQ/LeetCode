class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angle = abs((hour % 12) * 5 + (minutes / 60) * 5 - minutes)
        angle += (60 - 2 * angle) * (angle > 30)
        angle *= 6
        return angle
