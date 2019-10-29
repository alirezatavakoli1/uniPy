#Alireza Tavakoli

def triangular (xTri):
    
    sumVar  =   0
    
    for i in range( 0, 100000):
    
        if  sumVar  >  xTri:
            return False

        elif sumVar == xTri:
            return True
        
        else:
            sumVar  +=  i 
########################
def square (xSqu):
    
    temp    =   0

    for i in range( 0, 100000):
        
        if temp     >   xSqu:
            return False
        
        elif temp   ==  xSqu:
            return True
        
        else:
            temp = i**2
##########################
functionList    =   [ square, triangular]

while (True):
    try:
        num     =   int ( input ("Please, enter number: "))
    except ValueError as error :
        print (error)
        print ()
        continue

    if num  == -1 :
        print("******************************")
        print("| good bye see you later  ;) |")
        print("******************************")
        print()
        break
    
    elif  functionList[0](num) and functionList[1](num):
        print ("+--------------------------------------------+")
        print ("|This number is both a triangle and a square.|")
        print ("+--------------------------------------------+")
        print()

    elif  functionList[0](num) :
        print ("===================================")
        print ("||This number is a square number.||")
        print ("===================================")
        print ()

    elif functionList[1](num):
        print ("#####################################")
        print ("#This number is a triangular number.#")
        print ("#####################################")
        print ()

    else:
        print ("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        print ("&This number is neither a triangle nor a square number.&")
        print ("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        print ()


##End
