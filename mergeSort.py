def merge(arr,l,r,mid):
    n1 = mid-l+1
    n2 = r - mid
    L = [arr[i] for i in range(l,mid+1)]
    R = [arr[i] for i in range(mid+1,r+1)]
    i = 0
    j = 0
    k = l
    while(i <n1 and j < n2):
        if(L[i] <= R[j]):
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
            
        k+= 1
        
    while(i<n1):
        arr[k] = L[i]
        i += 1
        k+= 1
    while(j<n2):
        arr[k] = R[j]
        j += 1
        k += 1
    
    print(" merge ", L ," and ", R , " is ",arr[l:r+1] , " from ",l,"  to ",r)
    xl = True
    for i in range(n1):
        if(L[i]<L[i+1] ):
            xl = False
            break
    print(xl,"xl")
def mergeSort(arr,l,r):
    if(l<r):
        mid = (l+r-1)//2
        mergeSort(arr,l,mid)
        mergeSort(arr,mid+1,r)
        merge(arr,l,r,mid)
        

def main():
    arr = [1,7,5,3,7,9,4,2,7,5,3,11,6,1]
    mergeSort(arr,0,len(arr)-1)
    print(arr)

if (__name__ == "__main__"):
    main()
    
