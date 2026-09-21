class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
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

        
        # TRIED to use dict as a key to another dict
        # this doesn't work in python. so might as well
        # use an array instead of a dict for each string

        # listOfFreqs = [{} for _ in range(m)]

        # comparisonDict = {}

        # for i in range(m):
        #     for c in strs[i]:
        #         listOfFreqs[i][c] = listOfFreqs[i].get(c, 0) + 1
            
        #     key = listOfFreqs[i]
        #     if key not in comparisonDict
        #         ComparisonDict[key] = []
        #     comparisonDict[key].append(i)