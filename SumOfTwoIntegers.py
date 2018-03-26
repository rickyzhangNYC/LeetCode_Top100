import sys

def getSum(self, a, b):
    """
    :type a: int
    :type b: int
    :rtype: int
    """
    # 32 bits integer max
    MAX = 0x7FFFFFFF
    mask = 0xFFFFFFFF
    while b != 0:
        # Gets XOR of both integers "sum" without carry, mask is used to isolate 32 bits
        # Get carry bits, mask is used to isolate 32 bits
        # a and b calculated before being assigned new values
        a, b = (a ^ b) & mask , ((a & b) << 1) & mask
        
    # if a is negative, get a's 32 bits complement positive first
    # then get 32-bit positive's Python complement negative
    return a if a <= MAX else ~(a ^ mask)