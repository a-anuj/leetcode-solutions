class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        num1 = nums[:n]
        num2 = nums[n:]
        ans = []

        #[2,5,1] , [3,4,7]

        for i in range(0,n):
            ans.append(num1[i])
            ans.append(num2[i])
        return ans