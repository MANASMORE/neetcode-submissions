class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for i in range(len(strs)):
            key = ''.join(sorted(strs[i]))
            if key not in groups:
                groups[key] = [strs[i]]
            else:
                groups[key].append(strs[i])

        return list(groups.values())