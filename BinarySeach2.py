
def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high+low)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return binary_search(arr, mid+1, high, x)
        elif arr[mid] > x:
            return binary_search(arr, low, mid-1 , x)

    else:
        return -1


# arr
arr = [1, 2, 3, 4, 5, 6, 7, 8]
x = 7

# program
result = binary_search(arr, 0, len(arr)-1, x)
if result == -1:
    print("ERROR")
else:
    print(str(result))
