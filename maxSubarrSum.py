def maxCross(arr, l , m , r):
    maxSum = -1000000
    sum = 0
    for i in range(m,l-1,-1):
        sum += arr[i]
        if(sum > maxSum):
            maxSum = sum
    

    for i in range(m+1,r+1,1):
        sum += arr[i]
        if(sum > maxSum):
            maxSum = sum


    return maxSum

def maxSub(arr,l,r):
    if (l == r):
        return arr[l]
        
    m = l + (r-l)//2
    return max(maxSub(arr,l,m), maxSub(arr,m+1,r),maxCross(arr,l,m,r))

def main():
    arr = [2, 3, 4, 5, 7]
    n = len(arr)
    print(maxSub(arr, 0, n-1))

if __name__ == "__main__":
    main()


