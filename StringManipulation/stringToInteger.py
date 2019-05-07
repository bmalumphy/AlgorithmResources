class Solution(object):
    def myAtoi(self, string):
        """
        :type str: str
        :rtype: int
        """
        string = string.strip()
        final = ""
        finalInt = 0
        n = len(string)
        if(string == ""):
            return 0
        if(not string[0].isdigit() and not string[0] == "+" and not string[0] == "-"):
            return 0
        for i in range(0, n):
            # if(string[0].isdigit() or string[0] == "+" or string[0] == "-"):
            #     final += string[i]
            if(string[i] == " "):
                break
            if((string[i] == "-" or string[i] == "+") and i == 0):
                try:
                    if(string[i+1].isdigit()):
                        final = string[i]
                    
                    else:
                        break
                except:
                    break
            elif(string[i].isdigit()):
                final = final + string[i]
            else:
                break
                
        try:
            finalInt = int(final)
        except ValueError:
            pass
        if finalInt > 2147483647:
            finalInt = 2147483647
        elif finalInt < -2147483648:
            finalInt = -2147483648
            
        return finalInt
                