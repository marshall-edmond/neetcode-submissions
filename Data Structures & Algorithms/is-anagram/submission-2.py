class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #s and t are both strings
        #anagram means they contain the same letters, regardless of order

        #store letters and frequency as k:v in a set..

        s_map = {}

        #iterate through s and add each letter to the set
        for letter in s:
            if letter in s_map:
                s_map[letter] += 1;
            else:
                s_map[letter] = 1;

        for letter in t:
            if letter not in s_map: 
                return False
            elif letter in s_map:
                s_map[letter] -= 1;
                if s_map[letter] < 0:
                    return False

        for key in s_map:
            if s_map[key] != 0:
                return False
        return True