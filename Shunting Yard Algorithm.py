#Shunting Yard Algorithm by Miles Burne 5/6/18
#http://planetmath.org/shuntingyardalgorithm
#https://en.wikipedia.org/wiki/Shunting-yard_algorithm

def shuntingYard(infixEquation):
    infixEquation = infixEquation # the original infix equation
    postfixEquation = "" # output for the shunting yard, queue
    numberStack = [] # number stack in practice
    operationStack = [] #operator stack in practice
    BODMAS = {"(":1,")":1,"^":2,"/":3,"*":4,"+":5,"-":6} # tells shunting what BODMAS is and priority of operators

    #first iteration through INFIX
    for x in list(infixEquation):
        #what a waste of space for POSTFIX
        if x == " ":
            pass
        
        try:
            #test for number
            y = int(x)
            postfixEquation.append(x)
            
        except:
            #if not number than operator
            if (BODMAS[operationStack[len(operationStack)-1]] > BODMAS[x]) and (operationStack[len(operationStack)-1] != "("):
                operationPop = True
            else:
                operationPop = False
            #if operator at top of operationStack needs to be popped..
            while operationPop == True:
                operatorInsertion = operationStack.pop(len(operationStack)-1)
                postfixEquation.append(operatorInsertion)
                if (BODMAS[operationStack[len(operationStack)-1]] > BODMAS[x]) and (operationStack[len(operationStack)-1] != "("):
                    operationPop = True
                else:
                    operationPop = False
            #once used, now stored
            operationStack.append(x)
        



shuntingYard("5+5*6")
