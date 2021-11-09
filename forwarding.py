class KB:
    def __init__(self) -> None:
        self.premise = [] 
        self.conclusion = ""
        self.count = 0


agenda = [] 


#method to get inputs
def forwardChaining():
    KnowledgeBase = []
    inputs = "" 
    while(True):
        KBInput = input("Please input knowledge base:(type 'exit' if you want to stop)\n")
        if(KBInput == "exit"):
            break
        if(len(KBInput) == 1):
            agenda.append(KBInput)
            print("Agenda["+str(len(agenda) - 1)+ "]:",end="") #printing agenda input
            print(agenda[len(agenda) - 1])
            continue
        else:
            count = 0
            premiseIndex = 0  
            newKB = KB() #new knowledge base item each time
            while(KBInput[premiseIndex] != '='): 
                if(KBInput[premiseIndex] == '^'):
                    premiseIndex += 1
                else:
                    newKB.premise.append(KBInput[premiseIndex]) #add new premise to KB object
                    premiseIndex += 1
                    count += 1
            newKB.count = count
            newKB.conclusion = KBInput[-1]
            KnowledgeBase.append(newKB)

            for premiseValue in range(len(newKB.premise)):
                print("KB["+str(len(KnowledgeBase) - 1)+ "].premise["+ str(premiseValue) + "]:",end="") #printing KB inputs
                print(newKB.premise[premiseValue] + ", ",end="") 
            print("KB["+str(len(KnowledgeBase) - 1)+ "].conclusion ",end="")#print conclusion
            print(newKB.conclusion + ", ",end="")
            print("count: " + str(newKB.count))

    print("stopped")
    queryValue = input("What is your query?\n")
    
    print("=============")
    print("Forward chaning algorithm starts")
    print("=============")
    return(solveQuery(KnowledgeBase, queryValue))



def solveQuery(KB, query):
    inferred = {} #keeps track of symbols already gone through agenda
    for agendaValue in agenda: #add values to inferred, set to false
        inferred[agendaValue] = False

    for KBValue in KB: #add knowledge base symbols to inferred
        inferred[KBValue.conclusion] = False
        for i in KBValue.premise:
            inferred[i] = False
    
    while(len(agenda) != 0):
        poppedValue = agenda.pop(0)
        print(poppedValue)
        if poppedValue == query:
            return True
        if inferred[poppedValue] == False:
            inferred[poppedValue] == True
            for KBStatement in KB:
                if(poppedValue in KBStatement.premise):
                    KBStatement.count = KBStatement.count - 1
                    if(KBStatement.count == 0):
                        agenda.append(KBStatement.conclusion)
    return False
                    



print(forwardChaining())
