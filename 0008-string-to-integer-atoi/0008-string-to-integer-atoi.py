class Solution:
    def myAtoi(self, s: str) -> int:
        has_signed = False
        has_zero_leading = False
        has_number = False
        is_number_in = False
        lst = list()
        valid_chars = [" ", "+", "-"] + [str(i) for i in range(10)]

        for c in s:
            if c not in valid_chars: break

            if c == " ":
                if has_signed or has_zero_leading or has_number: break

            if c == "+" or c == "-":
                if has_signed or has_zero_leading or has_number: break
                else:
                    if c == "-": lst.append(c)
                    has_signed = True
                    continue

            if c == "0":
                if has_number: lst.append(c)
                else:
                    has_zero_leading = True
                    continue

            if "1" <= c <= "9":
                lst.append(c)
                has_number = True
                is_number_in = True

        if not is_number_in: return 0
        ans = int("".join(lst))
        if ans < -(2 ** 31): ans = -(2 ** 31)
        if ans > 2 ** 31 - 1: ans = (2 ** 31) - 1
        return ans
