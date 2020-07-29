class Solution:
    def uniqueOccurrences(self, arr) :
        nums_set = {}
        for num in arr :
            nums_set[num] = nums_set.get(num,0) + 1

        cnt = list(nums_set.values())

        for i in range(len(cnt)):
            if cnt[i] in cnt[i+1:] : return False
        return True

t = Solution()
t.uniqueOccurrences([1,2,2,1,1,3])