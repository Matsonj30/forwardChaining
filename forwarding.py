#Forwarding.py
#Forward chaining algorithm to dtermine if a symbol is True based on a set of given statements
#Takes statements in the form of characters: P=>Q, L^M=>Q, A, B etc. 
#** Will break if put in empty imput***
#Class KB
#This class represents each statement in the total KB, it will have a set of premises, and a conclusion

class KB:
    def __init__(self) -> None:
        self.premise = [] 
        self.conclusion = ""
        self.count = 0
        self.sentence = ""

agenda = [] 

#def forwardchaining()
#This method will ask the user to input implications and agenda values
#These values will create the knowledge base, which will be used to determine if the query is true based on the knowledge given

#Returns True or False, depending on if the query is solvable or not
def forwardChaining():
    KnowledgeBase = []
    while(True):
        KBInput = input("Please input knowledge base:(type 'exit' if you want to stop)\n").strip()
        if(KBInput == "exit"):
            break
        if(len(KBInput) == 1):
            agenda.append(KBInput)
            print("Agenda["+str(len(agenda) - 1)+ "]:",end="") #printing agenda input
            print(agenda[len(agenda) - 1])
            continue
        else: #if the input is not just a fact
            count = 0
            premiseIndex = 0  
            newKB = KB() #new knowledge base item each input
            newKB.sentence = KBInput
            while(KBInput[premiseIndex] != '='):  #get premises in the implication
                if(KBInput[premiseIndex] == '^'):
                    premiseIndex += 1
                else:
                    newKB.premise.append(KBInput[premiseIndex]) #add new premise to KB object
                    premiseIndex += 1
                    count += 1
            newKB.count = count #set count value of a implication
            newKB.conclusion = KBInput[-1] #set conclusion side of implication
            
            KnowledgeBase.append(newKB) #now that all values are put into the newly created KB class, we can append the object to the list
            #print each premise of the current KB input
            for premiseValue in range(len(newKB.premise)):
                print("KB["+str(len(KnowledgeBase) - 1)+ "].premise["+ str(premiseValue) + "]:",end="") #printing KB inputs
                print(newKB.premise[premiseValue] + ", ",end="") 
            print("KB["+str(len(KnowledgeBase) - 1)+ "].conclusion ",end="")#print conclusion
            print(newKB.conclusion + ", ",end="")
            print("count: " + str(newKB.count)) #print count

    print("stopped")
    queryValue = input("What is your query?\n")

    print("=============")
    print("Forward chaning algorithm starts")
    print("=============")
    print("")
    return(solveQuery(KnowledgeBase, queryValue))


#def solveQuery
#Given the knowledgeBase and the query, will utilize forward chaining
#To return wether the query is true or false based on the information given
#Parameters:
#KB - the knowledge base
#query - the query
#Returns: True or False
def solveQuery(KB, query):
    inferred = {} #keeps track of symbols already gone through agenda
    for agendaValue in agenda: #add agenda values to inferred, set to false
        inferred[agendaValue] = False

    for KBValue in KB: #add knowledge base premises to inferred, set to false
        inferred[KBValue.conclusion] = False
        for i in KBValue.premise:
            inferred[i] = False
    
    while(len(agenda) != 0):
        poppedValue = agenda.pop(0)
        print("***** Current agenda:" + poppedValue+ " *****")
        if poppedValue == query:
            print("Goal Achieved")
            print("The query " + str(query) + " is true based on the knowledge")
            print("---- The End -----")
            return True
        if inferred[poppedValue] == False: #make sure to not get in a loop
            inferred[poppedValue] == True
            for KBStatement in KB:
                if(poppedValue in KBStatement.premise): #looking for premises that use current agenda value
                    print(KBStatement.sentence +", ",end="")
                    print("count: " + str(KBStatement.count))
                    print("Premise "+ str(poppedValue)+ " matched agenda")
                    KBStatement.count = KBStatement.count - 1  #decrease and print new count
                    print("Count is reduced to "+ str(KBStatement.count),end="")
                    if(KBStatement.count == 0):
                        agenda.append(KBStatement.conclusion)
                        print("==> Agenda " + KBStatement.conclusion +" is created")
                    else:
                        print("")
            print("=============") 
    print("---- The End -----")
    return False
                    
print(forwardChaining())
