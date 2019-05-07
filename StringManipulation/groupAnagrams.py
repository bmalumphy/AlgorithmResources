def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        solutions = []
        hashMap = {}
        for string in strs:
            key = "".join(sorted(string))
            if key in hashMap:
                hashMap[key].append(string)
            else:
                hashMap[key] = [string]
        for lst in hashMap.values():
            solutions.append(lst)
        
        return solutions   