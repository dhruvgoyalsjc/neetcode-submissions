class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        freqs = {} # this is my hashmap/dict to keep track of counts

        freqsArr = [[] for _ in range(n+1)] # this is the list where index is count
        # and the value is a list of values with that count

        res = [] # this is what I return

        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1
        
        for num, cnt in freqs.items():
            freqsArr[cnt].append(num)

        # numReturned = 0 //don't need this
        for i in range(n, -1, -1):
            for val in freqsArr[i]:
                res.append(val)
                # numReturned += 1 //don't need this
                if len(res) >= k:
                    return res
        
        return res