def reverse_arr(arr,left,right):
    if left>=right:
        return
    arr[left],arr[right]=arr[right],arr[left]
    left=left+1
    right=right-1
    reverse_arr(arr,left,right)
arr=[1,2,3,4,5,6,7,8,9]
reverse_arr(arr,3,6)
print(arr)