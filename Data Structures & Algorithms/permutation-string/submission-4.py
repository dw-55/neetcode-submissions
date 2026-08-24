class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        first = 0
        last = len(s1)-1
        hashmap = {}
        if len(s1) > len(s2):
            return False
        for i in range (len(s1)):
            if hashmap.get(s1[i], 0) >= 1:
                hashmap[s1[i]] += 1
            else:
                hashmap[s1[i]] = 1
        for j in range(len(s1)):
            if s2[j] in hashmap:
                hashmap[s2[j]] -= 1
        all_zeros = all(val == 0 for val in hashmap.values())
        if all_zeros:
            return True
        while last != len(s2)-1:
            if s2[first] in hashmap:
                hashmap[s2[first]] += 1
            first += 1
            last += 1
            if s2[last] in hashmap:
                hashmap[s2[last]] -= 1
            all_zeros = all(val == 0 for val in hashmap.values())
            if all_zeros:
                return True
        return False
            