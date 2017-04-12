import numpy as np
from math import floor
class peakFind(object):
    """ Peak Finder Algorithm.

    Parameters
    -----------

    Methods
    ----------
    peak1D(arr) : method to identify peak for a 1D-array.
    peak2D(mat, startj, endj) : method to identify peak for a 2D-array.

    Attributes
    -----------
    value_ : value for the peak
    i_ : index for the peak/ row index for peak in case of a 2D array.
    j_ : column index for peak in case of a 2D array

    """

    def __init__(self):
        self.start = 0
        self.value = 0

    def peak1D(self, arr, start, end):
        """Find a peak in 1D-array.

        Function to find a peak (not all peaks) for a 1D-array
        Parameters
        -----------
        arr : {array-like}, shape = [n]
            array for which a local peak needs to be found

        Returns
        --------
        self : object

        """
        m = start + floor((end-start)/2)
        l = len(arr)-1
        if (m == 0 | m == l):
            self.i_ = m
            self.value_ = arr[m]
            return self

        elif arr[m-1] <= arr[m] >= arr[m+1]:
            self.i_ = m
            self.value_ = arr[m]
            return self

        elif arr[m-1] > arr[m]:
            return self.peak1D(arr, start, m-1)

        elif arr[m+1] > arr[m]:
            return self.peak1D(arr, m+1, end)


    def peak2D(self, mat, startj, endj):
        """Find a peak for a 2D-array.

        Function to find a peak (not all peaks) for a 1D-array.
        Parameters
        -----------
        mat : {2D array-like}, shape = [[j],[j],[j],....i]
            2D array list of lists for which a local peak
            needs to be found.
        startj : column index for start location of 2d array.
        endj: column index for end location of the 2d array.

        Returns
        --------
        self : object

        """
        jm = floor((endj - startj)/2)
        igmx = self.GlobMax([row[jm] for row in mat])

        if mat[igmx][jm-1] <= mat[igmx][jm] >= mat[igmx][jm+1]:
            self.value_ = mat[igmx][jm]
            self.i_ = igmx
            self.j_ = jm
            return self

        elif mat[igmx][jm-1] > mat[igmx][jm]:
            return self.peak2D([row[startj:jm] for row in mat],
                startj, jm-1)

        elif mat[igmx][jm+1] > mat[igmx][jm]:
            return self.peak2D([row[jm+1:] for row in mat],
                jm+1, endj)

    def GlobMax(self, arr):
        imx = self.start
        for i in range(len(arr)-1):
            if arr[i] < arr[i+1]:
                imx = i+1
        return imx


if __name__ == '__main__':
    peakFind()
