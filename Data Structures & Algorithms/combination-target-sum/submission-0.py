class Solution:
    def solve(self, index, total, subset, nums, target, result):
        if total == target:
            result.append(subset.copy())
            return

        if total > target or index >= len(nums):
            return

        # Take nums[index]
        subset.append(nums[index])
        self.solve(index, total + nums[index], subset, nums, target, result)

        # Don't take nums[index]
        subset.pop()
        self.solve(index + 1, total, subset, nums, target, result)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.solve(0, 0, [], candidates, target, result)
        return result