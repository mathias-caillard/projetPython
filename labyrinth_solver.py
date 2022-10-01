#Depth-first search in a labyrinth

import numpy as np


lab = np.array([[1 for k in range(1)] for k in range(1)])

CX = [-1,0,1,0]
CY = [0,-1,0,1]

L = 2
trial = 0
yes = False
compter = 0
rules = []
nodes = []
flag_nodes = False


def try_(X,Y,M,N,filename) :

    global yes
    global trial
    global L
    global lab
    global compter
    global nodes
    global rules
    global flag_nodes

    #initialization of nodes.
    if not flag_nodes :
        nodes.append("[X=" + str(X) + ", Y=" + str(Y) + "]")
        flag_nodes = True



    if (X==1) or (X==M) or (Y==1) or (Y==N) :
        yes = True
    else :
        K = 0
        while not yes and (K < 4) :
            K += 1
            U = X + CX[K-1]
            V = Y + CY[K-1]
            compter += 1

            if lab[U-1][V-1] == 0 :
                trial += 1
                L += 1
                lab[U-1][V-1] = L
                X_temporary_backtrack = U
                Y_temporary_backtrack = V
                with open(filename,'a') as f:
                    print(str(compter) + ") " + "-"*(L-3) + "R" + str(K) + ". U=" + str(U) + ", V=" + str(V) + ". " + "Free. " + "L:=L+1=" + str(L) + ". " + "LAB[" + str(U) + "," + str(V) + "]:=" + str(L),file=f)
                rules.append("R" + str(K))
                nodes.append("[X=" + str(U) + ", Y=" + str(V) + "]")
                try_(U,V,M,N,filename)
                if not yes : #backtrack
                    lab[U-1,V-1] = -1
                    L -= 1
                    with open(filename,'a') as f:
                        print("-"*(L-1) +  "Backtrack from " + "X=" + str(X_temporary_backtrack) + ", Y=" + str(Y_temporary_backtrack) + ", L=" + str(L+1) + ". lAB[" + str(U) + "," + str(V) + "]:=-1. L:=L-1=" + str(L),file=f)
                    rules.pop()
                    nodes.pop()

            elif lab[U-1][V-1] == 1 :
                with open(filename,'a') as f:
                    print(str(compter) + ") " + "-"*(L-3) + "R" + str(K) + ". U=" + str(U) + ", V=" + str(V) + ". " + "Wall.",file=f)
            else :
                with open(filename,'a') as f:
                    print(str(compter) + ") " + "-"*(L-3) + "R" + str(K) + ". U=" + str(U) + ", V=" + str(V) + ". " + "Thread.",file=f)



def labyrinth_solver(X_initial, Y_initial,M,N,filename) :

    global yes
    global trial
    global lab
    global L

    with open(filename,'a') as f:
        print("PART 1. Data",file=f)
        print("1.1. Labyrinth",file=f)
        print("",file=f)
        print(np.rot90(lab),file=f)
        print("1.2. Initial position X=" + str(X_initial) + ", Y=" + str(Y_initial) + ". L=" + str(L),file=f)
        print("",file=f)
        print("PART 2. Trace",file=f)

    L = 2
    lab[X_initial-1][Y_initial-1] = L
    yes = False
    trial = 0
    try_(X_initial,Y_initial,M,N,filename)

    with open(filename,'a') as f:
        print("",file=f)
        print("PART 3. Results",file=f)



    if yes :
        with open(filename,'a') as f:
            print("3.1. Path exists",file=f)
    else :
        with open(filename,'a') as f:
            print("3.1. Path does not exist",file=f)

    with open(filename,'a') as f:
        print("3.2. Path graphically:\n",file=f)
        print(np.rot90(lab),file=f)
        print("",file=f)
        print("absissa : X,U",file=f)
        print("ordinate : Y,V\n",file=f)
        print('3.3. Rules:',file=f)
        print(np.array(rules),file=f)
        print("3.4. Nodes:",file=f)
        print(np.array(nodes),file=f)


def reinitialize() :

    global L
    global trial
    global yes
    global compter
    global rules
    global nodes
    global flag_nodes

    L = 2
    trial = 0
    yes = False
    compter = 0
    rules = []
    nodes = []
    flag_nodes = False


def labyrinth_test() :

    global lab

    #test n°1

    reinitialize()

    lab = np.array([
     [1,1,1,1,1,0,1,],
     [1,0,0,0,1,0,1,],
     [1,0,1,0,1,0,1,],
     [1,0,0,0,1,0,1,],
     [1,1,1,0,0,0,1,],
     [1,1,1,1,1,0,0,],
     [1,1,1,1,1,0,1,]
     ])

    M = len(lab)
    N = len(lab[1])
    X_initial = 5
    Y_initial = 4

    labyrinth_solver(X_initial, Y_initial,M,N,"test1")

    #test n°2

    reinitialize()
    lab = np.array([
    [1,1,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,1,0,1],
    [1,0,1,0,1,0,1,0,1],
    [1,0,0,0,0,0,1,0,1],
    [1,0,1,0,1,0,1,0,1],
    [1,0,0,0,0,0,1,0,1],
    [1,0,1,0,1,0,1,0,1],
    [1,0,0,0,0,0,1,0,1],
    [1,1,1,1,1,0,1,0,1],
    [1,0,0,0,0,0,1,0,1],
    [1,0,1,1,1,1,1,0,1],
    [1,0,1,0,0,0,1,0,1],
    [1,0,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,1,0,1],
    [1,0,0,0,1,0,0,0,1],
    [1,1,1,1,1,1,1,1,1],
    ])

    M = len(lab)
    N = len(lab[1])
    X_initial = 9
    Y_initial = 6

    labyrinth_solver(X_initial, Y_initial,M,N,"test2")

    #test n°3

    reinitialize()
    lab = np.array([
    [1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
    [1,1,0,0,0,0,0,1,0,0,0,1,1,0,1],
    [1,1,0,1,1,1,1,1,0,1,0,0,0,0,1],
    [1,1,0,1,0,1,1,1,0,1,1,0,1,1,1],
    [1,1,0,1,0,1,1,1,0,1,1,0,1,1,1],
    [1,1,0,1,0,1,1,1,0,1,1,0,1,1,1],
    [1,1,0,1,0,1,1,1,0,1,1,0,1,1,1],
    [1,1,0,1,0,1,1,1,0,1,1,0,1,1,1],
    [1,1,0,1,0,0,0,0,0,1,1,0,1,1,1],
    [1,1,0,1,1,1,1,1,0,1,1,0,1,1,1],
    [1,0,0,0,0,0,0,1,0,1,1,0,1,1,1],
    [1,1,0,1,1,1,1,0,0,1,1,0,1,1,1],
    [1,1,0,0,0,1,0,0,1,1,1,0,1,1,1],
    [1,1,0,1,0,1,0,1,1,1,1,0,1,1,1],
    [1,1,0,1,0,1,0,1,1,1,1,0,1,1,1],
    [1,1,0,0,0,1,0,0,0,0,0,0,1,1,1],
    [1,1,1,0,0,0,0,0,1,0,1,1,0,1,1],
    [1,1,1,0,1,0,1,0,1,0,1,1,0,1,1],
    [1,1,1,1,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ])

    M = len(lab)
    N = len(lab[1])
    X_initial = 19
    Y_initial = 14
    labyrinth_solver(X_initial, Y_initial,M,N,"test3")







