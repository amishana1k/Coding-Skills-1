#Single Number

    def singleNumber(self, nums: List[int]) -> int:
        f={}
        
        for i in range(len(nums)):
            if i not in f:
                return i
