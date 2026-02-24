def Bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
        print(j)
    print(arr)
arr = [1, 5, 8, 9, 3, 2]
Bubble_sort(arr)


#Time complexity of selection sort is o(n^2)
#space complexity is o(1)