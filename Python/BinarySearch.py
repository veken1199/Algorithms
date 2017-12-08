# It takes an ordered array of integers and int target
# returns the position if the target is found in the array or -1 if not
def binarySearch(arr=[], target=-1):
    start = 0
    end = len(arr)

    while (start < end):

        mid = int((start + end) / 2)
        if (arr[mid] == target):
            return mid
        elif (arr[mid] > target):
            end = mid
        else:
            start = mid + 1

    return -1


print(binarySearch([1, 2, 3], 3))
