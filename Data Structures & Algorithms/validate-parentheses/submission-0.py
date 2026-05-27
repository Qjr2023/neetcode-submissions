class Solution:
    def isValid(self, s: str) -> bool:
        dictS = {"]" : "[", ")" : "(", "}" : "{"} 
        saveS = []
        for c in s:
            if c in dictS:
                if saveS and dictS[c] == saveS[-1]:
                    saveS.pop()
                else:
                    return False
            else:
                saveS.append(c)
        return True if not saveS else False