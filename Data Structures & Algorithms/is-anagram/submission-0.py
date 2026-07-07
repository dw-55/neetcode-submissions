class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapS = {}
        mapT = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] in mapS:
                value = mapS.get(s[i])
                mapS[s[i]] = value + 1
            else:
                mapS[s[i]] = 1
            if t[i] in mapT:
                value = mapT.get(t[i])
                mapT[t[i]] = value + 1
            else:
                mapT[t[i]] = 1

        if mapS == mapT:
            return True
        return False