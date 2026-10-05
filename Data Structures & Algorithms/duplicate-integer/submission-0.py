class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Nums is an integer array
        #True or false result
        #Track integers we've already seen in a set, and if the value is in the set return True... After the loop is complete return false

        seen_before = set()
        #For integer in the integer array
        for num in nums:
            if num in seen_before:
                return True
            else:
                seen_before.add(num)
        return False