#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Constriants 
    chk_bound = all(ele >= 1 and ele <= 100 for ele in ar) 
    if n in range(1,101) and len(ar) in range (1,n+1) and chk_bound:
        #ar_elements_count = dict(Counter(ar)) # Using collection.Counter to count repeated elemnents in the list
        ar_dict = {i:ar.count(i) for i in ar}
        ar_num_pairs = {k: ar_dict.get(k)//2 for k in ar_dict} # Find the number of Pairs of socks (quotient of each key in ar_dict by divisor 2)
        pair_sum = int(sum(ar_num_pairs.values()))
        #print (pair_sum)
        
    else:
        raise Exception(" Inpute Out of Bound ")
    return (pair_sum)
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    #fptr.write(str(result) + '\n')

    #fptr.close()
    print (result)