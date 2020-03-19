'''
# 1108. Defanging an IP Address
# https://leetcode.com/problems/defanging-an-ip-address/
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

'''
class Solution:
    def defangIPaddr(self, address: str) -> str:
        address = address.replace("." , "[.]")
        return print(address)

Test = Solution()
Test.defangIPaddr("1.1.1.1")