# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    merged_arr = []
    i = 0
    j = 0
    # TO-DO

    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            merged_arr.append(arrA[i])
            i += 1
        else:
            merged_arr.append(arrB[j])
            j += 1

    while i < len(arrA):
        merged_arr.append(arrA[i])
        i += 1

    while j < len(arrB):
        merged_arr.append(arrB[j])
        j += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[0:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


print(
    merge_sort(
        [
            123,
            4,
            2,
            42,
            31,
            3,
            234,
            1,
            23,
            23,
            443,
            523,
            55,
            463,
            45,
            345,
            4356,
            5,
            52,
            4,
            234,
            345,
            43,
            3,
        ]
    )
)

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
