class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        maximum=0          
        for i in range(0, len(nums)):
        # Reset count when 0 is found
            if (nums[i] == 0):
                count = 0
 
        # If 1 is found, increment count
        # and update result if count
        # becomes more.
            else:
             
            # increase count
                count+= 1
                maximum = max(maximum, count)
        
        return maximum