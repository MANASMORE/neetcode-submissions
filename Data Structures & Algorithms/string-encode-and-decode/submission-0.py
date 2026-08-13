class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded = encoded + str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
        
            n = int(s[i:j])
            i = j + 1

            word = s[i:i + n]
            ans.append(word)
            i = i + n
        return ans