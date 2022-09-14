counter = 1
begin = True
the_end = False
initial_n = 0
A = []
B = []
C = []


def initialize_global_variable():

    global counter
    global begin
    global initial_n
    global the_end

    counter = 1
    begin = True
    the_end = False
    initial_n = 0



def hanoi(n,start,intermediate,end) :
    # A : start
    # B : intermediate
    # C : end
    # n : number of disks FOR THE CALL

    global counter
    global begin
    global initial_n
    global the_end
    global A
    global B
    global C
    global plug_A_name
    global plug_B_name
    global plug_C_name

    # initial_n is the number of disks AT THE INITIAL CALL

    #Allow to display the begin message, initialization

    if begin :
        print("Yaay !! The algorithm begins !")
        print("")
        begin = False
        initial_n = n
        A = [n-k for k in range(n)]
        plug_A_name = start
        plug_B_name = intermediate
        plug_C_name = end

        #print the states of plugs
        print("plug A --> " + str(A))
        print("plug B --> " + str(B))
        print("plug C --> " + str(C))
        print("")




    if n > 0 and n < 11 :

        #Move n disks from A to C
        if n == 1 :
            print("Step " + str(counter) + " : " + "move disk " + str(n) + " from " + start + " to " + end)
            counter += 1




            if start == plug_A_name :
                start_plug = A
            elif start == plug_B_name :
                start_plug = B
            elif start == plug_C_name :
                start_plug = C

            if end == plug_A_name :
                end_plug = A
            elif end == plug_B_name :
                end_plug = B
            elif end == plug_C_name :
                end_plug = C

            disk = start_plug.pop()
            end_plug.append(disk)


            print("plug A --> " + str(A))
            print("plug B --> " + str(B))
            print("plug C --> " + str(C))
            print("")

        else :
            #Move n-1 disks from A to B
            hanoi(n-1, start, end, intermediate)


            #Move the disk n from A to C
            print("Step " + str(counter) + " : " + "move disk " + str(n) + " from " + start + " to " + end)
            counter += 1

            if start == plug_A_name :
                start_plug = A
            elif start == plug_B_name :
                start_plug = B
            elif start == plug_C_name :
                start_plug = C

            if end == plug_A_name :
                end_plug = A
            elif end == plug_B_name :
                end_plug = B
            elif end == plug_C_name :
                end_plug = C

            disk = start_plug.pop()
            end_plug.append(disk)


            #print the states of plugs
            print("plug A --> " + str(A))
            print("plug B --> " + str(B))
            print("plug C --> " + str(C))
            print("")



            #Move n-1 disks from B to C
            hanoi(n-1, intermediate, start, end)

            # Allow to display the end message
            if 2**initial_n - 1 == counter-1 :
                if not the_end :
                    print("Oh noo... The algorithm ends...")
                    the_end = True



    else :

        print("The number n of disks must be between 1 and 10 included.")