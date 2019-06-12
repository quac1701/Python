global arr
arr =  [0,0,0,0,0,0,0,0]

def ucv(k,i):
    if(i ==0 ):
        return True
    else:
        for j in range (i):
            if(k == arr[j] or arr[j] - j == k - i ):
                return False
            
        return True

def show(n):
    for i in range(n):
        print(i,arr[i])

def xepHau(i):
    if(i == 7):
        show(8)
    else:
        for k in range(8):
            print(ucv(k,i),"ucv")
            if(ucv(k,i)):
                arr[i] = k 
                show(i)
                print(i)               
                xepHau(i+1)

xepHau(0)
             