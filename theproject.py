import random as rand
import numpy as np
#Idea
#Recursion, Loops, If statement, Random
#Input array length
#Randomize inputs in length of a 2d array (Random)
#Use numpy to transpose the array
#recursive badly the longest length continously Horizontal/Vertical


#makes the array as a 2d array (list type)
def makelist(len,wid):
    #empty lists
    arraylist = []
    rowlist = []
    #loops the bottom comment wid amount of times
    for x in range(0,wid):
        for i in range(0,len):
            #appends a random int from 0,1 (0 or 1 in this case) to the rowlist for len amount of times
            rowlist.append(rand.randint(0,1))
        #appends the rowlist
        arraylist.append(rowlist)
        #clears rowlist to repeat 
        rowlist = []
    return arraylist


#displays array to console in a square format
def printarray(myarray):
    for i in myarray:
        print(i)
    print()

def streak(myarray):
    maxcountlist = []
    #counter is a variable which counts the streak
    counter = 0
    #maxcounter keeps track of the longest streak when it breaks
    maxcounter = 0
    #for row in my array
    for i in myarray:
        #for item in the row in my array
        for x in i:
            #check if its 1 (on)
            if x == 1:
                counter = counter + 1
            #if 0 (off), records max counter and resets counter
            else:
                if counter > maxcounter:
                    maxcounter = counter
                    counter = 0
                else:
                    counter = 0
            #prevents error if the max streak is end of row like 01111
            if counter > maxcounter:
                maxcounter = counter

            #print(x, end = '')
        #print()
        #print(f'counter = {maxcounter}')
        #resets counters for next row and then appends to a list of max counts
        maxcountlist.append(maxcounter)
        counter = 0
        maxcounter= 0
        #print()
    return maxcountlist

def transposelist(myarray):
    #turns nested list from horizontal to vertical using numpy
    arraynump = np.array(myarray)
    trans = arraynump.transpose()
    #converts back to nested list
    vertarray = trans.tolist()
    
    '''
    print('------')
    for i in arraynump:
        print(i)
    print('------')
    transarraynump = arraynump.transpose()
    for i in transarraynump:
        print(i)
    '''
    return vertarray

#prints hiphens to length of the list printed statement (for formatting)
def printdivide(len):
    len = len * 3
    for i in range(len):
        print('-',end='')
    print()
    print()

    
    
#gather input
widthlist = int(input("Input the width of the array"))
heightlist = int(input("Input the height of the array"))
print()

#makes array
myarray = makelist(widthlist,heightlist)

#transposes list
mytranspose = transposelist(myarray)

#gets max streak in horizontal
print("Horizontal List")
printarray(myarray)
printdivide(widthlist)
horizontallist = streak(myarray)

#gets max streak in vertical
print("Vertical List")
printarray(mytranspose)
verticallist = streak(mytranspose)


print(f'The longest streak horizontally is {max(horizontallist)}')
print(f'The longest streak vertically is {max(verticallist)}')
'''
print(horizontallist)
printdivide(widthlist)
print(verticallist)
'''
#print(widthlist,heightlist)
