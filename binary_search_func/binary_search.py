def binary_search(arr: list, target: int)->int:
    """
    binary search example
    array must be sorted
    Args:
        *sorted,
        *arrayvalue
    Returns:
        *index of target in array or possible index
    """
    # setting up left and right pivots
    left, right = 0, len(arr)-1
    while(left<=right):
        # getting middle index
        middle = left + (right-left)//2
        if arr[middle] == target:
            # return found index of target
            return middle
        elif arr[middle] > target:
            # decrease of right pivot
            right = middle - 1
        elif arr[middle] < target:
            # increase of left pivot
            left = middle + 1
    # if target not in array return possible index with minus
    return -(left+1)

if __name__ == "__main__":
    arr = [-2,-1,0,1,2,3,4,5,10,12]
    print(binary_search(arr,7))