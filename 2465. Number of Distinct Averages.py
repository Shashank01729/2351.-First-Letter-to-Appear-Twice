class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        l=sorted(nums)
        s=set()
        while l:
            a=l.pop(0)
            b=l.pop()
            s.add((a+b)/2)
        return len(s)