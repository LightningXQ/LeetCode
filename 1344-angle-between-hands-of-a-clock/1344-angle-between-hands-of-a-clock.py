class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_pos = (hour % 12) * 5 + (minutes / 60) * 5
        minutes_pos = minutes

        angle = abs(hour_pos - minutes_pos)
        if angle > 30: angle = 60 - angle
        angle *= 6
        return angle
