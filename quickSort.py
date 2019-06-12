def partition(arr, l , r):
    pos = l -1
    pivot = arr[r]
    for i in range(l,r+1):
        if (pivot >= arr[i]):
            pos += 1            
            arr[pos] , arr[i] = arr[i] , arr[pos]

    return (i)

def quickSort(arr, l ,r):
    if (l <r):
        pi = partition(arr,l,r)
        quickSort(arr,l,pi-1)
        quickSort(arr,pi+1,r)

def main():
    arr = [1,28,6,3,8,9,4,6,12,4,52,1]
    quickSort(arr,0,len(arr)-1)
    print(arr)

if __name__ == "__main__":
    main()