#!/bin/python3

import os
import itertools

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def permute(w):
    pass

def biggerIsGreater(w):
    # Write your code here
    p_list = permute(w)
    int_list = []
    for word in p_list:
        int_value = int(''.join(str(ord(c)-ord('a')) for c in word))
        int_list.append(int_value)
        
    int_list.sort(reverse=True)
    index = int_list.index(int(''.join(str(ord(c)-ord('a')) for c in w)))
    return ''.join(chr(c+ord('a')) for c in int_list[index+1])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
