class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(index, currCombo, comboSum):
            # base case good
            if comboSum == target:
                res.append(currCombo.copy())
                return
            # base case bad
            if index >= len(nums) or comboSum > target:
                return

            # recursive case
            
            # either we add another instance of nums[index] and don't
            # change index
            currCombo.append(nums[index])
            dfs(index, currCombo, comboSum + nums[index])
            # or we increment index and recurse, undo the change
            # to currCombo and thus no change to comboSum
            currCombo.pop()
            dfs(index + 1, currCombo, comboSum)
        
        # initial recursive call
        dfs(0, [], 0)
        return res
            
            