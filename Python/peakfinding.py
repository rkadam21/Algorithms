import numpy as np
from math import floor

def findPeak(arr):
    '''Find a peak in 1D-array.

    Function to find a peak (not all peaks) for a 1D-array

    '''
    mid = floor(len(arr)/2)
    print("The mid is: ", mid)
    check = True
    i = mid
    l = len(arr)-1
    while check == True:
        if (i==0 | i==l):
            check=False
        elif arr[i-1] > arr[i]:
            i=i-1
        elif arr[i+1] > arr[i]:
            i=i+1
        elif ((arr[i] == arr[i+1]) & (arr[i] != arr[i-1])):
            i=i+1
        elif ((arr[i] != arr[i+1]) & (arr[i] == arr[i-1])):
            i=i-1
        else:
            check = False
    print("The index of the peak is: ", i)

if __name__ == '__main__'
    findPeak()
