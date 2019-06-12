from quickSort import quickSort

def binarySearch(arr, l, r,x):
    if r >= l :
        pos = int(l + (r-l)/2)
        if (arr[pos] == x):
            return pos

        elif (arr[pos]<x):
            return binarySearch(arr,pos+1,r,x)

        elif (arr[pos]>x):
            return binarySearch(arr,l,pos-1,x)
    
    else:
        return -1

def main():
    arr = [4,2,4,6,87,2,44,1,23,4,55,6,2,7,1,2]
    quickSort(arr,0,len(arr)-1)
    print(arr)
    print(binarySearch(arr,0,len(arr)-1,23))
    print(binarySearch(arr,0,len(arr)-1,2))

if __name__ == "__main__":
    main()


