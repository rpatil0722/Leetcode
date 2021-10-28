class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for i in range(0,len(nums)):
            if(len(str(nums[i]))%2==0):
                count=count+1
            else:
                continue
        return count