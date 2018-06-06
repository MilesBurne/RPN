#Shunting Yard Algorithm by Miles Burne 5/6/18
#http://planetmath.org/shuntingyardalgorithm
#https://en.wikipedia.org/wiki/Shunting-yard_algorithm


def shuntingYardAlgo(infixEquation):
    infixEquation = infixEquation # the original infix equation
    postfixEquation = [] # output for the shunting yard, queue
    numberStack = [] # number stack in practice
    operationStack = [] #operator stack in practice
    BODMAS = {"(":1,")":1,"^":2,"/":3,"*":4,"+":5,"-":6} # tells shunting what BODMAS is and priority of operators
    associative = {"^":"R","*":"L","/":"L","+":"L","-":"L"}
    
    if len(infixEquation) != 0:
        conversionLoop = True
        infixPos = 0 #position of number/letter
    while conversionLoop == True:
        #get token
        print(postfixEquation)
        token = list(infixEquation)[infixPos]
        #read the token
        try:
            x = int(token) #if token is number
            postfixEquation.append(x)
            
        except: #token not number
            
            #if token is operator
            if token in BODMAS:
                while len(operationStack) != 0: # while operator stack is not empty
                    if (BODMAS[token] < BODMAS(operationStack[-1:])) or ((BODMAS[token] == BODMAS[operationStack[-1:]]) and (associative[operationStack[-1:]])) == ("L" and operationStack[-1:] != "("):
                        postfixEquation = operationStack.pop() #pop from stack to equation
                    else:
                         break
                operationStack.append(token)

            #if token is left bracket
            if token == "(":
                operationStack.append(token)

            #if token is a right bracket
            if token == ")":
                while len(operationStack) != 0:
                    if operationStack[-1:] != "(":
                        postfixEquation = operationStack.pop() #pop from stack to equation
                    else:
                        break
                if len(operationStack) == 0 and postfixEquation[-1:] != "(":
                        print("Mismatched brackets")
                        quit()

                operationStack.pop() #pop left bracket from stack

            #checking if end
            if len(infixEquation) != 0:
                while len(operationStack) != 0:
                    postfixEquation.append(operationStack.pop())
                conversionLoop = True
                infixPos = 0 #position of number/letter
        infixPos += 1
    return(postfixEquation) #end




print(shuntingYardAlgo("5+5*6"))
