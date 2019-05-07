class Solution:
    def removeInvalidParentheses(self, s: 'str') -> 'List[str]':                    
        if not s: return [""]
        q = [(s, 0, 0, '(', ')')]
        ans = []        
        while q:
            tmps, i0, j0, p0, p1 = q.pop()
            len_s = len(tmps)
            invalid = False
            counter = 0
            for index in range(i0, len_s):
                if tmps[index] == p0: counter += 1
                elif tmps[index] == p1: counter -= 1
                if counter < 0:
                    invalid = True
                    break
            if not invalid:
                if p1 == ')':
                    q.append((tmps[::-1], 0, 0, p1, p0))
                else:
                    ans.append(tmps[::-1])
            else:
                for j in range(j0, index + 1):
                    if tmps[j] == p1 and (j == j0 or tmps[j-1] != p1):
                        q.append((tmps[:j] + tmps[j+1:], index, j, p0 , p1))                        
        return ans