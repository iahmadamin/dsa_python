def search_target(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = int((left + right) / 2)
        print(arr[mid])
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1


if __name__ == '__main__':
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = int(input("Enter target: "))
    result = search_target(arr, target)
    if result == -1:
        print("Target does not exists in array.")
    else:
        print(str(target)+" is at "+str(result)+" index")