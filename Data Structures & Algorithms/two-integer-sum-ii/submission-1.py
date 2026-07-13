class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo, high = 0, len(numbers) - 1
        while numbers[lo] + numbers[high] != target:
            s = numbers[lo] + numbers[high]
            if s > target:
                high -= 1
            elif s < target:
                lo += 1
        return [lo + 1, high + 1]