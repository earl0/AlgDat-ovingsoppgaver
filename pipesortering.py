#!/usr/bin/python3

from sys import stdin


def sort_list(A):
    # Sort the list using a simple version of quick sort
    quicksort(A, 0, len(A) - 1)
    return A

def quicksort(A, lo, hi):
    if lo < hi:
        p = partition(A, lo, hi)
        quicksort(A, lo, p - 1)
        quicksort(A, p + 1, hi)

def partition(A, lo, hi):
    pivot = A[hi]
    i = lo - 1
    for j in range(lo, hi):
        if A[j] < pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    i += 1
    if A[hi] < A[i]:
        A[i], A[hi] = A[hi], A[i]
    return i

def find(A, lower, upper):
    # The initial index range is the whole array
    lowerIndex = 0
    upperIndex = len(A) - 1
    # If the target lower value is inside the array, find it
    if lower > A[lowerIndex]:
        lowerIndex = findIndex(A, 0, upperIndex, lower)
    # If the target upper value is inside the array, find it
    if upper < A[upperIndex]:
        upperIndex = findIndex(A, lowerIndex, upperIndex, upper)
    # Assert that we are on the right value and not the neighbor
    if A[lowerIndex] > lower and lowerIndex > 0:
        lowerIndex -= 1
    if A[upperIndex] < upper and len(A) - 1 > upperIndex:
        upperIndex += 1
    return [A[lowerIndex], A[upperIndex]]
    
def findIndex(A, begin, end, value):
    if begin >= end:
        return end
    middle = int((begin + end) / 2) # Find the middle point
    if A[middle] < value:
        # We below the value, look higher up in the list
        return findIndex(A, middle + 1, end, value)
    if A[middle] > value:
        # We are above the value, look lower down in the list
        return findIndex(A, begin, middle - 1, value)
    return middle;

def main():
    input_list = []
    for x in stdin.readline().split():
        input_list.append(int(x))

    sorted_list = sort_list(input_list)

    for line in stdin:
        word = line.split()
        minimum = int(word[0])
        maximum = int(word[1])
        result = find(sorted_list, minimum, maximum)
        print(str(result[0]) + " " + str(result[1]))

if __name__ == "__main__":
    main()