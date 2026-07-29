class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Cannot be Anagrams if they don't have the same length
        if len(s) != len(t):
            return False

        #K:V map of S, Key is letter : V is frequency
        map_of_s = {

        }
        
        
        for index, letter in enumerate(s):
            if letter in map_of_s:
                map_of_s[letter] += 1

            else:
                map_of_s[letter] = 1

        for letter in t:

            if letter not in map_of_s:
                return False
            if letter in map_of_s:
                map_of_s[letter] -= 1
                
                if map_of_s[letter] < 0:
                    return False

        return True