class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = [""] * numRows
        row = 0
        direction = 1

        if numRows==1:
            return s

        for i in range(len(s)):
            if row==0:
                ans[row] += s[i]
                direction = 1
            elif row == numRows-1:
                ans[row] += s[i]
                direction = -1
            else:
                ans[row] += s[i]

            row += direction
        return "".join(ans)