import numpy as np
from math import floor

def findPeak(arr):
    '''Find a peak in 1D-array.

    Function to find a peak (not all peaks) for a 1D-array

    '''
    mid = floor(len(arr)/2)
    check = True
    i = mid
    l = len(arr)-1
    while check == True:
        if (i==0 | i==l):
            check=False
        elif arr[i-1] <= arr[i] >= arr[i+1]:
            check = False
        elif arr[i-1] > arr[i]:
            i=i-1
        elif arr[i+1] > arr[i]:
            i=i+1
    return i

def find2DPeak(mat, startj, endj):
    '''Find a peak for a 2D-array.

    '''
    jm = floor((endj - startj)/2)
    igmx = GlobMax([row[jm] for row in mat])
    if mat[igmx][jm-1] <= mat[igmx][jm] >= mat[igmx][jm+1]:
        return (igmx, jm)
    if mat[igmx][jm-1] > mat[igmx][jm]:
        return find2DPeak([row[startj:jm] for row in mat], startj, jm-1)
    if mat[igmx][jm+1] > mat[igmx][jm]:
        return find2DPeak([row[jm+1:] for row in mat], jm+1, endj)

find2DPeak(mat,0,4)
def GlobMax(arr):
    imx=0
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            imx = i+1
    return imx

if __name__ == '__main__':
    findPeak()
