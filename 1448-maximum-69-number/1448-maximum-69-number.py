class Solution(object):
    def maximum69Number (self, num):
        lst = list(str(num))

        for i in range(len(lst)):
            if lst[i] == "6":
                lst[i] = "9"
                break

        return int("".join(lst))
