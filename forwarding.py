class KB:
    def __init__(self) -> None:
        self.premise = [] 
        self.conclusion = ""
        self.count = 0

inferred = {} #keeps track of symbols already gone through agenda
agenda = [] 
KnowledgeBase = []

#method to get inputs
def forwarding():
    inputs = "" 
    while(inputs != 'exit'):
        KBInput = input("Please input knowledge base:(type 'exit' if you want to stop)\n")
        if(len(KBInput) == 1):
            agenda.append(KBInput)
            continue
        else:
            count = 0
            premiseIndex = 0  
            newKB = KB()
            while(KBInput[premiseIndex] != '='): 
                if(KBInput[premiseIndex] == '^'):
                    premiseIndex += 1
                else:
                    newKB.premise.append(KBInput[premiseIndex])
                    premiseIndex += 1
                    count += 1
            newKB.count = count
            newKB.conclusion = KBInput[-1]
            KnowledgeBase.append(newKB)
            print(KnowledgeBase[-1].premise)
            print(KnowledgeBase[-1].conclusion)

forwarding()