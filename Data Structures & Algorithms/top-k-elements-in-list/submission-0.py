class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Freq = {}
        ans = []
        max_freq = 0

        for i in range(len(nums)):
            if nums[i] not in Freq:
                Freq[nums[i]] = 1
            else:
                Freq[nums[i]] += 1
            
        for num in Freq:
            if Freq[num] > max_freq:
                max_freq = Freq[num]

        while max_freq > 0 and len(ans) < k:
            for n in Freq:
                if Freq[n] == max_freq:
                    ans.append(n)

                    if len(ans) == k:
                        break
            max_freq -= 1
    
        return ans