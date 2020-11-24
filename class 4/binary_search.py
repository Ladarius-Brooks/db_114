def binary_search(arr,ele):
    first = 0 
    last = len(arr) -1
    found = False
    while first <= last and not found:
        mid = int((first+last)/2)

        if arr[mid] == ele:
            found True

        else:
            if ele < arr[mid]:
                last = mid -1
            else:
                first = mid + 1

        return found