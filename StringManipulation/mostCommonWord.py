import string

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        nopunc = paragraph.translate(str.maketrans(string.punctuation, ' '*len(string.punctuation))).lower()
        #print(nopunc)
        
        words = nopunc.split(" ")
        #print(words)
        
        actuallyADictionary = {}
        for i in words:
            if not i in banned and i:
                if i in actuallyADictionary:
                    actuallyADictionary[i] += 1
                else:
                    actuallyADictionary[i] = 1
        solution = []
        if not actuallyADictionary:
            return ""
        maxCount = max(actuallyADictionary.values())
        for key, value in actuallyADictionary.items(): 
            if maxCount == value: 
                return key