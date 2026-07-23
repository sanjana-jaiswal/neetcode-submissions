class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenHash={}
        for index,number in enumerate(nums):
            difference=target-number
            if difference in seenHash:
                return [seenHash[difference],index]
            seenHash[number]=index