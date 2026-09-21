class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        comparisonDict = defaultdict(list)

        for s in strs:
            freqs = [0] * 26
            for c in s:
                freqs[ord(c) - ord('a')] += 1
            
            #add strings to a list corresponding to a value
            #associated with each different frequency
            comparisonDict[tuple(freqs)].append(s)
        
        return list(comparisonDict.values())

        """
        ---------------------
        use default dicsts to make life easier
        also don't need to store indexes you can just map the
        freq to the actual string
        """

        """
        m = len(strs)

        comparisonDict = {}

        # get arrays of len 26 to represent char frequencies
        for i in range(m):
            freqs = [0] * 26
            for c in strs[i]:
                freqs[ord(c) - ord('a')] += 1
            
            # need to make into a tuple to be able to use as a map key
            # basically adding each index to the list of indexes 
            # corresponding to each anagram
            key = tuple(freqs)
            if key not in comparisonDict:
                comparisonDict[key] = []
            comparisonDict[key].append(i)
        
        # need this syntax so that the list objects are all different
        resultList = [[] for _ in range(len(comparisonDict))]
        i = 0
        for key in comparisonDict:
            for index in comparisonDict[key]:
                resultList[i].append(strs[index])
            i += 1
        # ^ just adding each anagram to its own list
        return resultList
        """

        """
        TRIED to use dict as a key to another dict
        this doesn't work in python. so might as well
        use an array instead of a dict for each string
        """

        # listOfFreqs = [{} for _ in range(m)]

        # comparisonDict = {}

        # for i in range(m):
        #     for c in strs[i]:
        #         listOfFreqs[i][c] = listOfFreqs[i].get(c, 0) + 1
            
        #     key = listOfFreqs[i]
        #     if key not in comparisonDict
        #         ComparisonDict[key] = []
        #     comparisonDict[key].append(i)