class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        length = 0
        seq = set(nums)
        for num in seq:
            if num - 1 not in seq:
                length = 1
                while num + length in seq:
                    length += 1
            
                longest = max(longest, length)

        return longest
