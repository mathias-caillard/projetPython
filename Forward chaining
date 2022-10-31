

#forward chain
import copy


def main_program(filename) :
    with open("D:/Vilnius_2A/IA/forward_chain/" + filename,'a') as fw:
        with open("D:/Vilnius_2A/IA/forward_chain/input_file.txt") as f:
            lines = f.readlines()
            pointer = 3

            humanLines = []
            machineLines = []
            facts = []
            goal = []

            #rules (humans)
            humanLine = lines[pointer]
            while humanLine != "\n" :
                humanLines.append(humanLine)
                pointer += 1
                humanLine = lines[pointer]
            #print(humanLines)

            #rules (machine)
            for humanLine in humanLines :
                pointer2 = 0
                while humanLine[pointer2] != "/" :
                    pointer2 += 1

                machineLine = humanLine[:pointer2]
                machineLines.append(machineLine.replace(" ",""))



            #facts
            pointer += 2
            factsLine = lines[pointer]
            for fact in factsLine :
                if fact != " " and fact != "\n":
                    facts.append(fact)


            #goal
            pointer += 3
            pointerGoal = 0
            tmpGoal = lines[pointer][0]
            goal = [tmpGoal]



        #Part 1. Data
        # 1.1) Rules
        print("Part 1. Data\n",file=fw)
        print("1) Rules",file=fw)
        compter_rules = 0
        for rule in machineLines :
            compter_rules += 1
            localGoal = rule[0]
            localFacts = ""
            factPointer = 1
            while factPointer < len(rule) :
                localFacts = localFacts + rule[factPointer]
                if factPointer != len(rule)-1 :
                    localFacts = localFacts + ","
                factPointer += 1

            print("R" + str(compter_rules) + ": " + str(localFacts) + " -> " + localGoal,file=fw)

        #1.2) Facts

        factsString = ""
        factPointer = 0
        while factPointer < len(facts) :
            factsString = factsString + facts[factPointer]
            if factPointer != len(facts) - 1:
                factsString = factsString + ", "
            factPointer += 1
        print("2)  Facts " + factsString,file=fw)

        #1.3) Goal
        print("3) Goal " + goal[0] + "\n",file=fw)

        #Part 2. Trace
        print("PART 2. Trace",file=fw)
        iterationCompter = 0
        rulesCompter = 0
        change = True
        factsEvolving = copy.copy(facts)
        flag1 = [False for rule in machineLines]
        flag2 = [False for rule in machineLines]

        flag1_tmp = [False for rule in machineLines]
        flag2_tmp = [False for rule in machineLines]

        Path = []

        while change and (not goal[0] in factsEvolving) :
            change = False
            iterationCompter += 1
            print("\nITERATION " + str(iterationCompter) + "\n",file=fw)

            rulesCompter = 1
            for rule in machineLines :

                localGoal = rule[0]
                localFacts = listToString(rule[1:])


                if localGoal in factsEvolving :
                    print("R" + str(rulesCompter) + ": " + str(localFacts) + " -> " + localGoal + " not applied, because result in facts. Raise flag2.",file=fw)
                    flag2_tmp[rulesCompter-1] = True


                elif allElement(rule[1:],factsEvolving) :
                    if (not flag1[rulesCompter-1]) and (not flag2[rulesCompter - 1]) :



                        factsEvolving.append(localGoal)
                        factsStringEvolvedFiltered = listToString(AminusB(factsEvolving,facts))

                        print("R" + str(rulesCompter) + ": " + str(localFacts) + " -> " + localGoal + " apply. Raise flag1. Facts " + factsString + " and " + factsStringEvolvedFiltered,file=fw)
                        flag1_tmp[rulesCompter-1] = True
                        change = True
                        Path.append("R" + str(rulesCompter))



                    if flag1[rulesCompter-1] :
                        print("R" + str(rulesCompter) + ": " + str(localFacts) + " -> " + localGoal + " skip, because flag1 raised.",file=fw)

                    elif flag2[rulesCompter -1] :
                        print("R" + str(rulesCompter) + ": " + str(localFacts) + " -> " + localGoal + " skip, because flag2 raised.",file=fw)


                else :
                    lackingFactsString = listToString(AminusB(rule[1:], factsEvolving))
                    print("R" + str(rulesCompter) + ": " + str(localFacts) + " -> " + localGoal + " not applied, because of lacking " + lackingFactsString,file=fw)

                rulesCompter += 1


                flag1_pointer = 0
                while flag1_pointer < len(flag1) :
                    flag1[flag1_pointer] = flag1[flag1_pointer] or flag1_tmp[flag1_pointer]
                    flag1_pointer += 1

                flag2_pointer = 0
                while flag2_pointer < len(flag2) :
                    flag2[flag2_pointer] = flag2[flag2_pointer] or flag2_tmp[flag2_pointer]
                    flag2_pointer += 1

        #part 3. Results
        print("\nPART 3. Results",file=fw)
        if not change :
            print("1) Goal :" + goal[0] + " not achieved.",file=fw)
            print("2) Path : no path",file=fw)

        else :
            PathString = listToString(Path)
            print("1) Goal " + goal[0] + " achieved.",file=fw)
            print("2) Path : " + PathString + ".",file=fw)







#Helpers
def allElement(L1,L2) :
    for e in L1 :
        if e not in L2 :
            return False
    return True

def AminusB(A,B) :
    res = []
    for a in A :
        if a not in B :
            res.append(a)
    return res

def listToString(L) :
    pointer = 0
    res = ""
    while pointer < len(L) :
        res = res + str(L[pointer])
        if pointer != len(L) - 1 :
            res = res + ", "
        pointer += 1
    return res







