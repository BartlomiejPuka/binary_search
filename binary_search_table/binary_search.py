
def find_kth_smallest_num(n, m, k):
    left, right = 1, n*m
    while left < right:
        mid = left + (right-left)//2
        if has_atleast_k_smallers(mid, n, m, k):
            right = mid
        else:
            left = mid + 1
    return left

def has_atleast_k_smallers(x,n,m,k):
    smallers = 0
    for i in range(1,m+1):
        smallers += min(n, x//i)
    return smallers >= k

if __name__ == "__main__":
    A = [1,2,3,5,7,11,13,17,19,21,23]
    result = find_kth_smallest_num(100,70,50)
    print(result)