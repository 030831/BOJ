def solution(arr):

    del arr[arr.index(min(arr))]
    
    if arr:
        return arr
    else:
        return [-1]