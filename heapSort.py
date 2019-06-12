def heapify(arr,n,i):
    max = i
    l = 2*i+1
    r = 2*i+2
    if(l<n and arr[i] < arr[l]):
        max = l

    if(r<n and arr[max] < arr[r]):
        max = r

    if(max != i):
        arr[max] , arr[i] = arr[i] , arr[max]
        heapify(arr,n,max)

def heapSort(arr):
    for i in range(len(arr)-1, -1 , -1):
        heapify(arr,len(arr),i)

    for i in range(len(arr)-1, 0, -1):
        arr[0], arr[i] = arr[i],arr[0]
        heapify(arr,i,0)

def main():
    arr = [5,23,12,6,3,5,3,9,11]
    heapSort(arr)
    print(arr)

if __name__ == "__main__":
    main()
