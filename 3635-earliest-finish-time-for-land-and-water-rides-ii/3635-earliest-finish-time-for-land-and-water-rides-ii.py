class Solution:
    def earliestFinishTime(self, landStartTime: list[int], landDuration: list[int], waterStartTime: list[int],
                           waterDuration: list[int]) -> int:
        land_to_water = None
        water_to_land = None

        # land => water
        l_end = 200001
        w_end = 300001

        for l_s_t, l_d in zip(landStartTime, landDuration):
            if l_end > l_s_t + l_d:
                l_end = l_s_t + l_d

        for w_s_t, w_d in zip(waterStartTime, waterDuration):
            w_s_t = max(l_end, w_s_t)
            if w_end > w_s_t + w_d:
                w_end = w_s_t + w_d

        land_to_water = w_end

        # water => land
        l_end = 300001
        w_end = 200001

        for w_s_t, w_d in zip(waterStartTime, waterDuration):
            if w_end > w_s_t + w_d:
                w_end = w_s_t + w_d

        for l_s_t, l_d in zip(landStartTime, landDuration):
            l_s_t = max(w_end, l_s_t)
            if l_end > l_s_t + l_d:
                l_end = l_s_t + l_d

        water_to_land = l_end

        return min(land_to_water, water_to_land)
