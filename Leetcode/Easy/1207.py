# 1207. Unique Number of Occurrences
# https://leetcode.com/problems/unique-number-of-occurrences/

class Solution:
    def uniqueOccurrences(self, arr) :
        nums_set, nums = {}, []
        for num in arr : 
            if not num in nums : 
                nums.append(num)
                nums_set[num] = 1
            else : nums_set[num] += 1


        # for num in arr : 
            # nums_set[num] = num_set.get(num,0) +1

        keys = list(nums_set.values())

        for i in range(len(keys)):
            for c_key, n_key in zip(keys, keys[i+1:]):
                if c_key == n_key : return False
        return True

'''
같은 기능 간소화
        for i in range(len(keys)):
            if keys[i] in keys[i+1:] : return False
        return True
'''

t = Solution()
t.uniqueOccurrences([1,2,2,1,1,3])