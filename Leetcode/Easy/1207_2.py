class Solution:
    def uniqueOccurrences(self, arr) :
        nums_set = {}
        for num in arr :
            nums_set[num] = nums_set.get(num,0) + 1

# set은 중복 허용 X, 길이 비교를 해서 확인 가능
        return len(nums_set.values()) == len(set(nums_set.values()))
        

t = Solution()
t.uniqueOccurrences([1,2,2,1,1,3])