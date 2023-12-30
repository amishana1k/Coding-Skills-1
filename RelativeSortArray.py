#Relative Sort Array

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        l=[]
        l1=[]
        for i in arr2:
            for k in arr1:
                if i==k:
                    l.append(i)
        for i in arr1:
            if i not in arr2:
                l1.append(i)
        l1.sort()
                
        return l+l1
