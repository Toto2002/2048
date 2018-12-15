from copy import deepcopy
from random import randint
size = 4

def main():
    #  array=[[],[],[],[]]
    # for i in array:
    #      i.extend([0,0,0,0])
    # array[-1][-1]=2
    # array[-1][-2]=2
    # array[-1][-3]=2
    # array[-1][-4]=2
    array = []
    for i in range(size):
        array.append([])
        for z in range(size):
            array[i].append(0)
    array = addNumber(array)
    printa(array)
    while(True):                            
        x = input("-> ")  
        if(x=="w"):
            array = transpose(collapse(transpose(array)))
        if(x=="a"):
            array = collapse(array)
        if(x=="s"):
            array= transpose(list(map(myReverse,collapse(map(myReverse,transpose(array))))))
        if(x=="d"):
            array =  list(map(myReverse, collapse( map(myReverse,array))))
        if(x=="e"):
            break
        array = addNumber(array)
        printa(array)
        
        
def printa(array):
    for i in array:
        for x in i:
            print(x, "\t", end='')
        print()

def collapseRow(array):
    newArray = []
    newnewArray = []
    Jibletsskip = False
    for i in array:
        if i != 0 :
            newArray.append(i)
    newArray.append(0)
    for i in range(0,len(newArray)-1):
        if Jibletsskip == False:
            if newArray[i] == newArray[i+1]:
                newnewArray.append(newArray[i] + newArray[i+1])  
                Jibletsskip = True 
            else:
                newnewArray.append(newArray[i])
        else:
            Jibletsskip = False
    for i in range(0,len(array) - len(newnewArray)) : 
        newnewArray.append (0)
    return newnewArray


def collapse(grid):
    newGrid = []
    for row in grid:
        x = collapseRow(row)
        newGrid.append (x)
    return newGrid

def myReverse(l):
    return list(reversed(l))

def transpose(grid):
    grid2 = deepcopy(grid)
    for i in range(len(grid)):
        grid2[i] = []
        for row in grid:
            grid2[i].append(row[i])
    return grid2

def addNumber(grid):
    sumof0 = 0
    for row in grid:
        for i in row:
            if i==0:
                sumof0 = sumof0+1
    boogie = randint(0,sumof0)
    counter = 0
    for y, row in enumerate(grid):
        for x, i in enumerate(row):
            if i==0:
                if boogie == counter:            
                    grid[y][x] = randint(1,2)*2
                counter = counter+1
    return grid
    

    


            
    



main()