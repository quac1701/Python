import numpy as np
import random


price = np.array(np.int_(np.random.random((10,10))*100))
adapt = list(range(12))
root = []

def initPop():
    global root
    root = [random.sample(range(10),10) for i in range(12)]  # có cần để root thỏa mãn hàm thích nghi

def evaluate():
    global adapt
    for i in range(12):
        # print(root)
        adapt[i] = np.sum([price[j] for j in [(l,root[i][l]) for l  in range(10)]]) #Tổng price root[i]
        if(np.sum([i not in root[i] for i in range(10)]) != 0):
            adapt[i] += 1000000
        
    # nếu có trùng lặp thì +1000000
    adapt = np.array(adapt)

def select():
    global root
    tmp = sorted(adapt)[:]
    limit = tmp[int(12*80/100)]
    for i in range(12):
        if(adapt[i] > limit):
            root[i] = random.sample(range(10),10)

    #Chọn độ thích nghi > 80% và random ra các thế hệ mới 


def crossover():
    global root
    for j in range(20):
        (fa ,mo ) = random.sample(range(12),2)

        #ver1

        (pos1 ,pos2 ) = random.sample(range(10),2)
       
        for cut in range (min(pos1,pos2) , max(pos1,pos2)+1):
            tmpFa = root[fa][cut]
            tmpMo = root[mo][cut]
            root[fa][cut] , root[mo][cut] = root[mo][cut] ,root[fa][cut]
            for i in range(10):
                if(root[fa][i] == tmpMo):
                    root[fa][i] = tmpFa
            for i in range(10):
                if(root[mo][i] == tmpFa):
                    root[mo][i] = tmpMo

            
            print(root[fa],root[mo])

        #ver2 
        # for i in range len(fa):
        #     t = i
        #     while():
        #         mo[fa[t]] = t
        #         t = fa[t]


            
                

            
    # Giao phối lặp 20 lần cắt 1 điểm random 


def mutation():
    global root
    for j in range(20):
        child = random.randrange(12)
        (pos1 , pos2 )= random.sample(range(10),2)
        root[child][pos1] , root[child][pos2] = root[child][pos2], root[child][pos1]

    #Đột biến lặp 20 lần đảo vị trí 2 con bất kì 



def printStatus():
    print(sorted(adapt)[0])

def main():
    initPop()
    for l in range(100):
        evaluate()
        printStatus()
        crossover()
        mutation()
        select()
    

if __name__ == "__main__":
    main()
    