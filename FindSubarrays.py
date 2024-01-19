from collections import Counter
from typing import List

class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        counter_dict = Counter(nums)
        for count in counter_dict.values():
            if count > 1:
                return True
        return False
