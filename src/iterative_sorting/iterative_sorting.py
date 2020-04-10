array = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
# TO-DO: Complete the selection_sort() function below


def selection_sort(arr):
    def swap(arr, idx1, idx2):
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]

    # loop through n-1 elements
    for i in range(len(arr)):
        cur_index = i
        for j in range(i + 1, len(arr)):
            if arr[cur_index] > arr[j]:
                print(arr[cur_index], arr[j])
                cur_index = j

        swap(arr, i, cur_index)

    return arr


print("select_sort", selection_sort(array))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    def swap(arr, idx1, idx2):
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]

    for i in range(len(arr)):
        for j in range(i - 1):
            if arr[j] > arr[j + 1]:
                swap(arr, j, j + 1)

    return arr


print("bubble", bubble_sort(array))

# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
