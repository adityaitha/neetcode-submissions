class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        buckets = []
        result = []
        for _ in range(len(nums)+1):
            buckets.append([])
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 1
            else:
                hashmap[nums[i]] += 1
        for num in hashmap:
            freq = hashmap[num]
            buckets[freq].append(num)
        for a in range(len(nums),0,-1):
            for num in buckets[a]:
                result.append(num)
                if len(result) == k:
                    return result