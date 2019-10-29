#Alireza Tavakoli

def swap ( xswap, yswap):

        if ( yswap > xswap):
           temp    =   yswap
           yswap   =   xswap
           xswap   =   temp
##################
def GCD ( xGCD, yGCD):
 
    swap ( xGCD, yGCD)
    
    while (True):

        if ( yGCD == 0 ): break

        temp = xGCD % yGCD
        xGCD = yGCD
        yGCD = temp
    
    return xGCD
#################
def LCM ( xLCM, yLCM):
 
    LCM = ( xLCM * yLCM )/GCD(xLCM,yLCM)
    
    return LCM 
#################
try:
number1    =   int ( input ( 'please,enter  a number       ==>> '))
number2    =   int ( input ( 'please,enter another number  ==>> '))
except ValueError as error :
        print (error)
        print ()
        continue

print ('\n\n')

tempGCD     =   GCD ( number1 , number2)
print ("#######=============")
print ("# GCD #     %u     #" %tempGCD)
print ("####################")
print ("#######=============")
print ("# LCM #     %u     #"  %LCM ( number1 , number2))
print ("####################\n")

massege     =   "Have a Good Time"
print ( "%s" %massege)

