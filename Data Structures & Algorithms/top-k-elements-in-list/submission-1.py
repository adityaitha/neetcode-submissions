class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        buckets = []
        for i in range(len(nums)+1):
            buckets.append([])
        for n in nums:
            count[n] = 1 + count.get(n,0)
        for n in count:
            buckets[count[n]].append(n)
        result = []
        for a in range(len(buckets)-1,0,-1):
            for n in buckets[a]:
                result.append(n)
                if len(result) == k:
                    return result
     