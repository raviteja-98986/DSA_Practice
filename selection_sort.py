def selection_sort(arr):
    for i in range(len(arr)):
        min=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]
    print(arr)

arr=[1,5,8,9,3,2]
selection_sort(arr)

#Time complexity of selection sort is o(n(n+1)/2) ie o(n^2)
#space complexity is o(1)