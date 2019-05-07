class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        solution = []
        if not logs:
            return solution
        letterLogs = []
        digitLogs = []
        for log in logs:
            split = log.split()
            if split[1].isdigit():
                digitLogs.append(log)
            else:
                letterLogs.append([split[0], " ".join(split[1:])])
       
        letterLogs.sort(key = lambda l: (l[1], l[0]))
        letterLogs = [" ".join(key) for key in letterLogs]
        solution+=letterLogs
        solution+=digitLogs
        return solution