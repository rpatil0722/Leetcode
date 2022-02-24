#Solution1:

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]: 
        n=len(nums)
        left, right = 0, n - 1
        index = n - 1
        #result = [0 for x in arr]
        q=[0 for x in nums]
        while index >= 0:
            if abs(nums[left]) >= abs(nums[right]):
                q[index] = nums[left] * nums[left]
                left += 1
            else:
                q[index] = nums[right] * nums[right]
                right -= 1
            index -= 1
        
        return q


******************************************
#Solution2:

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(0,len(nums)):
            nums[i]*=nums[i]
        nums.sort()
        return nums