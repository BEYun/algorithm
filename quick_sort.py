def quick_sort(arr):
    def swap(arr, a, b):
        arr[a], arr[b] = arr[b], arr[a]

    def partition(left, right):
        if left >= right:
            return

        pivot = left
        i = left+1
        j = right
        while i <= j:
            while i <= j and arr[i] <= arr[pivot]:
                i += 1

            while i <= j and arr[j] >= arr[pivot]:
                j -= 1

            if i <= j:
                swap(arr, i, j)

        swap(arr, pivot, j)

        partition(left, j)
        partition(j+1, right)
    return partition(0, len(arr)-1)

n = [9, 7, 5, 11, 12, 2, 14, 3, 10, 6]
quick_sort(n)
print(n)