# 1450. Number of Students Doing Homework at a Given Time
# https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        cnt = 0
        for i in range(len(startTime)):
            time = list(range(startTime[i],endTime[i]+1))
            if queryTime in time : cnt += 1
        return cnt

T = Solution()
T.busyStudent(startTime = [1,2,3], endTime = [3,2,7], queryTime = 4)