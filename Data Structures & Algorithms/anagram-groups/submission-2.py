class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord("a")] += 1
            count = tuple(count)
            hashmap[count] = hashmap.get(count, [])
            hashmap[count].append(word)
        return list(hashmap.values())