class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            s = f"{len(s)}#{s}"
            result += s
        return result
    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            len_string = int(s[i:j])
            string = s[j+1:j+1+len_string]
            result.append(string)
            i=j+1+len_string
        return result

             
