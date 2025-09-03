class Solution(object):
    def rearrangeArray(self, nums):
        neg = [] * (len(nums)/2)
        pos = [] * (len(nums)/2)

        answer = [1]*len(nums)

        for i in nums:
            if i<0:
                neg.append(i)
            else:
                pos.append(i)
                        
        left1=0
        left2=0
        for i in range(len(nums)):
            if i%2==0:
                answer[i] = pos[left1]
                left1+=1
            else:
                answer[i] = neg[left2]
                left2+=1
        
        return answer

        