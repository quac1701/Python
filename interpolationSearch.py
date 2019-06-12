def interSearch(arr,n,x):
    l = 0
    r = n -1
    while( l<=r and x >= arr[l] and x <= arr[r]):
        pos = l + int(((r - l)/(arr[r]- arr[l]))*(x-arr[l]))
        print(pos)
        if arr[pos] == x:
            return pos
        if arr[pos] < x:
            l = pos + 1;
        else:
            r = pos - 1;     
    return -1

arr = [1,2,3,4,6,8,9,11,23,56,89]
print(interSearch(arr,len(arr),8),"res")