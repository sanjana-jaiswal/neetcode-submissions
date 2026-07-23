# Using Brute force
# class Solution:
#     def twoSum(self,nums:List[int],target:int)->List[int]:
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i]+nums[j]==target:
#                     return [i,j]
#         return[]

class Solution:
    def twoSum(self,nums:List[int],target:int)->List[int]:
        seenNumberMap={}
        for index,number in enumerate(nums):
            difference=target-number
            if difference in seenNumberMap:
                return [seenNumberMap[difference],index]
            seenNumberMap[number]=index