import numpy as np

N = 5  #Length of the board
NN = N**2 # number of square on the board

board = [[0]*N for i in range(N)]
CX = [0]*8
CY = [0]*8
compter = 0


def initialize() :

    CX[0] = 2
    CX[1] = 1
    CX[2] = -1
    CX[3] = -2
    CX[4] = -2
    CX[5] = -1
    CX[6] = 1
    CX[7] = 2

    CY[0] = 1
    CY[1] = 2
    CY[2] = 2
    CY[3] = 1
    CY[4] = -1
    CY[5] = -2
    CY[6] = -2
    CY[7] = -1

    for i in range(1,N+1) :
        for j in range(1,N+1):
            board[i-1][j-1] = 0

def try_(L,X,Y,filename,long) :

    global compter
    global globalg
    global yes

    #U, V : new knight's position
    K = 0 #Production number

    while (not yes) and K < 8 :


        K = K + 1
        U = X + CX[K-1]
        V = Y + CY[K-1]
        compter += 1





        if (U >= 0) and (U <= N-1) and (V >= 0) and (V <= N-1) :
            if board[U][V] == 0 :
                board[U][V] = L
                with open(filename,'a') as f:
                    if long :
                        print(str(compter) + ") " + "-"*(L-2) + "R" + str(K) + ". " + "U=" + str(U) + ", V=" + str(V) + ". " + "L=" + str(L) + ". Free. " + "BOARD[" + str(U) + "]" + "[" + str(V) + "]" + ":=" + str(L) + ".", file=f)

                if L < NN :
                    try_(L+1,U,V,filename,long)
                    if not yes :
                        board[U][V] = 0
                        with open(filename,'a') as f:
                            if long :
                                print(str(compter) + ") "+ "-"*(L-2) + "R" + str(K) + ". " + "U=" + str(U) + ", V=" + str(V) + ". " + "L=" + str(L) + ". Out. Backtrack.", file=f)
                else :
                    yes = True

            else :
                with open(filename,'a') as f:
                    if long :
                        print(str(compter) + ") " + "-"*(L-2) + "R" + str(K) + ". " + "U=" + str(U) + ", V=" + str(V) + ". " + "L=" + str(L) + ". Thread.",file=f)

        else :
            with open(filename,'a') as f:
                if long :
                    print(str(compter) + ") "+ "-"*(L-2) + "R" + str(K) + ". " + "U=" + str(U) + ", V=" + str(V) + ". " + "L=" + str(L) + ". Out. ",file=f)


def main_program(X_initial, Y_initial,filename,N_value, long) :

    global yes
    global N
    global NN
    global compter
    global board
    N = N_value
    NN = N**2
    compter = 0
    board = [[0]*N for i in range(N)]


    with open(filename,'a') as f:
        print("PART  1. Data",file=f)
        compter_ = 1
        print(str(compter_) + ") " + "Board: " + str(N) + "x" + str(N),file=f)
        compter_ += 1
        print(str(compter_) + ") " + "Initial position: X=" + str(X_initial) + ", Y=" + str(Y_initial) + ", L=1.",file=f)
        print("",file=f)
        if long :
            print("PART 2. Trace",file=f)

    initialize()
    yes = False

    board[X_initial][Y_initial] = 1
    try_(2,X_initial,Y_initial, filename,long)

    with open(filename,'a') as f:
        print("",file=f)
        print("PART 3. Results",file=f)


    if yes :

        with open(filename,'a') as f:
            print("1) Path is found. Trials : " + str(compter),file=f)
            print("2) Path graphically :",file=f)
            print(np.array(board),file=f)

    else :
        with open(filename,'a') as f:
            print("Path does not exist.",file=f)


def knight_solver() :

    #test 1
    main_program(0,0,'out-long1.txt',5,True)
    main_program(0,0,'out-short1.txt',5,False)

    #test 2
    main_program(4,0,'out-long2.txt',5,True)
    main_program(4,0,'out-short2.txt',5,False)

    #test 3
    main_program(0,4,'out-long3.txt',5,True)
    main_program(0,4,'out-short3.txt',5,False)

    #test 4
    main_program(1,0,'out-long4.txt',5,True)
    main_program(1,0,'out-short4.txt',5,False)

    #test 5
    main_program(0,0,'out-long5.txt',6,True)
    main_program(0,0,'out-short5.txt',6,False)

    #test 6
    main_program(0,0,'out-long6.txt',7,True)
    main_program(0,0,'out-short6.txt',7,False)

    #test 7
    main_program(0,0,'out-long7.txt',4,True)
    main_program(0,0,'out-short7.txt',4,False)




