
def binary_search(arr, target):
    if sorted(arr) != arr:
        binary_search(sorted(arr), target)
    elif any([not isinstance(x, int) for x in arr]):
        raise f"{arr} should be full of integers"
    left, right = 0, len(arr)-1
    while(left<=right):
        middle = left + (right-left)//2
        if arr[middle] == target:
            return middle
        elif arr[middle] > target:
            right = middle - 1
        else:
            left = middle + 1
    return -(left+1)

def find_twosums(arr, targets_sum):
    """
    Instead of two fors we can use solution below to find indexes of two elements which sums
    is equal to targets_sum
    """
    for first_index, first_num in enumerate(arr):
        second_num = targets_sum - first_num
        second_index = binary_search(arr, second_num)
        if second_index > 0 and first_index != second_index:
            yield first_index, second_index

if __name__ == "__main__":
    A = [1,2,3,5,7,11,13,17,19,21,23]
    result = find_twosums(A, 7)
    result = [(x, y) for (x, y) in result if x < y]
    values = [(A[x],A[y]) for (x, y) in result]
    print(f"indexes {result}", f"values {values}",sep="\n")