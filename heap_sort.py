import sys

def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]

def heap_sort(arr):
    def heapify(arr, arr_size):
        p = (arr_size // 2) - 1
        while(p>=0):
            shiftdown(arr, p, arr_size)
            p -= 1
    
    def shiftdown(arr, i, arr_size):
        l = 2*i + 1
        r = 2*i + 2
        largest = i
        if l <= arr_size-1 and arr[l] > arr[i]:
            largest = l
        if r <= arr_size-1 and arr[r] > arr[largest]:
            largest = r
        if largest != i:
            swap(arr, largest, i)
            shiftdown(arr, largest, arr_size)

    for i in range(len(arr), 1, -1):
        heapify(arr, i)
        swap(arr, 0, i-1)


n = int(sys.stdin.readline())
n_list = []
for _ in range(n):
    n_list.append(int(sys.stdin.readline()))

heap_sort(n_list)

for i in n_list:
    print(i)