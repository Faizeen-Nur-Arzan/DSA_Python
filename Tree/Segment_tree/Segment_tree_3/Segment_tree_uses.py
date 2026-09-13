# Python3 program to show segment tree operations like construction, query and update
from math import ceil, log2

# A utility function to get the middle index from corner indexes.
def getMid(s, e):
    return s + (e - s) // 2

"""
A recursive function to get the sum of values in the given range of the array. The following are parameters for this function.

st --> Pointer to segment tree
si --> Index of current node in the segment tree.
Initially 0 is passed as root is always at idex 0
ss & se --> Starting and ending indexes of the segment represented by the current node, i.e., st[si]
qs & qe --> Starting and endng indexes of query range
"""
def getSumUtil(st, ss, se, qs, qe, si):
    # if segment of this node is apart of given range, then return the sum of the segment
    if (qs <= ss and qe >= se):
        return st[si]
    
    # If segment of this node is outside the given range
    if (se < qs or ss > qe): 
        return 0
    
    # If a part of this segment overlaps with the given range
    mid = getMid(ss, se)

    return (getSumUtil(st, ss, mid, qs, qe, 2 * si + 1) + getSumUtil(st, mid + 1, se, qs, qe, 2 * si + 2))