# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 10:45:01 2017

@author: Arnulfo
"""

def longsub(s):
    for i in range(1,len(s)):
        if s[i-1]>s[i]:
            return s[:i]
    return s
def long_sub_search(longest,s):
    if s and (len(s)>len(longest)) :
        long_substring = longsub(s)
        if len(long_substring) > len(longest):
            longest = long_substring
        length = len(longest)
        if length < len(s):
            return long_sub_search(longest,s[length-1:])
        else:
            return longest
    else:
        return longest
    
s = 'azcbobobegghakl'

print(long_sub_search("",s))
        