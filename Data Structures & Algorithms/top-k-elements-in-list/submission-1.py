class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = {}
        # n = len(nums)
        res = []

        for n in nums:
            a[n] = a.get(n, 0) + 1
        
        sorted_items = sorted(a.items(), key=lambda item: item[1], reverse=True)
        
        for i in range(k):
            res.append(sorted_items[i][0])

        return res