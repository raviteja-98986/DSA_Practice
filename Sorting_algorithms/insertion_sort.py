def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
    print(arr)

arr = [1, 5, 8, 9, 3, 2]
insertion_sort(arr)

#Time complexity of insertion sort is o(n(n+1)/2) ie o(n^2)
#space complexity is o(1)