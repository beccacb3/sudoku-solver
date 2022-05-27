import numpy as np

#approaches
#backtracking - geeksforgeeks
#bit mask

#constraint statisfaction? hamiltonian circuits

#TODO
#sparse matrix for sudoku expansion
#reinforcement learning
#computer vision for reading in sudoku

def defaults():
    before = np.zeros((9,9), dtype=int)

    #row one
    before[0,0]=4
    before[0,1]=2
    before[0,5]=3
    before[0,7]=8
    before[0,8]=1

    #row two
    before[1,2]=1
    before[1,8]=3

    #row three
    before[2,1]=7
    before[2,2]=8
    before[2,4]=1
    before[2,5]=5
    before[2,7]=6
    before[2,8]=9

    #row four
    before[3,3]=6
    before[3,7]=3
    before[3,8]=5

    #row five
    before[4,0]=2
    before[4,1]=5
    before[4,2]=7
    before[4,6]=9
    before[4,7]=4
    before[4,8]=6

    #row six
    before[5,5]=9
    before[5,8]=8

    #row seven
    before[6,0]=1
    before[6,1]=9
    before[6,3]=2
    before[6,4]=8
    before[6,5]=4

    #row eight
    before[7,0]=7
    before[7,1]=4
    before[7,2]=5
    before[7,3]=3
    before[7,5]=6
    before[7,8]=2

    #row nine
    before[8,3]=1
    before[8,4]=5
    before[8,6]=6

    after= np.array([[4,2,9,7,6,3,5,8,1],[5,6,1,9,2,8,4,7,3],[3,7,8,4,1,5,2,6,9],[9,8,4,6,7,2,1,3,5],[2,5,7,8,3,1,9,4,6],[6,1,3,5,4,9,7,2,8],[1,9,6,2,8,4,3,5,7],[7,4,5,3,9,6,8,1,2],[8,3,2,1,5,7,6,9,4]])
    return before, after

x,y = defaults()
print(x)
print(y)

