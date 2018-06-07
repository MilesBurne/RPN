#Shunting Yard Algorithm by Miles Burne 5/6/18
#http://planetmath.org/shuntingyardalgorithm
#https://en.wikipedia.org/wiki/Shunting-yard_algorithm


def shuntingYardAlgo(infixEquation):
    infixEquation = infixEquation # the original infix equation
    postfixEquation = [] # output for the shunting yard, queue
    numberStack = [] # number stack in practice
    operationStack = [] #operator stack in practice
    BODMAS = {"(":1,")":1,"^":2,"/":3,"*":4,"+":5,"-":6} # tells shunting what BODMAS is and priority of operators
    associative = {"^":"R","*":"L","/":"L","+":"L","-":"L","(":"G",")":"G"} # "G" to prevent key errors
    
    if len(infixEquation) != 0:
        conversionLoop = True
        infixPos = 0 #position of number/letter

    while conversionLoop == True:
        #in program display of workings
        '''
        print("     "+str(infixPos))
        print(infixEquation[infixPos])
        print("PE: ", postfixEquation)
        print("OP: ", operationStack)
        '''
        #get token
        token = list(infixEquation)[infixPos]
        #read the token
        try:
            x = int(token) #if token is number
            postfixEquation.append(str(x))
            
        except: #token not number
    
            #if token is operator
            if token in BODMAS:
                
                while len(operationStack) != 0: # while operator stack is not empty
                    if (BODMAS[token] > BODMAS[str(operationStack[len(operationStack)-1])]) or ((BODMAS[token] == BODMAS[str(operationStack[len(operationStack)-1])]) and (associative[str(operationStack[len(operationStack)-1])])) == "L" and (operationStack[len(operationStack)-1] != "("):
                        if token != "(" and token != ")" and (operationStack[len(operationStack)-1] != "("):
                            postfixEquation.append(operationStack.pop()) #pop from stack to equation
                        else:
                            break
                    else:
                         break
                if token != "(" and token != ")":
                    operationStack.append(token)

            #if token is left bracket
            if token == "(":
                operationStack.append(token)

            #if token is a right bracket
            if token == ")":
                #backLoop = len(operationStack)
                for x in operationStack:
                    if len(operationStack) != 0:
                        if operationStack[len(operationStack)-1] != "(":
                            postfixEquation.append(operationStack.pop()) #pop from stack to equation
                        else:
                            break
                if "(" not in operationStack:
                        print("Mismatched brackets")
                        quit()
                operationStack.pop() #pop left bracket from stack

        infixPos += 1  
        #checking if end
        if infixPos == len(infixEquation):
            while len(operationStack) != 0:
                postfixEquation.append(operationStack.pop())
            conversionLoop = False
            infixPos = 0 #position of number/letter
            break
        
    return("".join(postfixEquation)) #end

while True:
    equation = input("Please enter the desired INFIX equation: ")
    print("Equation:         ", equation)
    print("Postfix equation: ", shuntingYardAlgo(equation))
