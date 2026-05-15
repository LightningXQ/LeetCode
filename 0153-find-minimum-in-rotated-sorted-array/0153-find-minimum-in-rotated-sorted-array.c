int findMin(int* nums, int numsSize) {
    int l = 0;
    int m = (numsSize - 1) / 2;
    int r = numsSize - 1;
    int lv, mv, rv;

    while (1) {
        lv = nums[l];
        mv = nums[m];
        rv = nums[r];

        if (lv == mv) {
            if (mv > rv) return rv;
            else return mv;
        }

        if (mv < rv) r = m;
        if (rv < mv) l = m;
        m = (l + r) / 2;
    }
}
