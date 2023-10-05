
#NAME

"""
#--------------------------------------------------
# integers.py
#--------------------------------------------------
"""

#DESCRIPTION

"""
#--------------------------------------------------
# A module with functions that are designed to help
# deal with most basic integer tasks
#--------------------------------------------------
"""

#FUNCTIONS

#-------------------------------------------------------

"""
# Answers the Question: Is this number Prime?
# Finds if the given number is a Prime Number or not
# returns a boolean True or False Statement to the question
"""


def isprime(Variable):

    # Answers the Question: is this number Prime?
    # Finds if the given number is a Prime Number or not
    # returns a boolean True or False Statement to the question

    import stdio

    FactorCounter = 0
    variable = Variable

    if variable < 1:
        return ("INVALID INTEGER: Only excepts input of integers higher than 1")

    if variable > 1:
        for i in range(2, variable):
            if variable % i != 0:
                pass
            if variable % i == 0:
                FactorCounter +=1
                break

    Answer = FactorCounter

    if Answer == 1:
        return (False)
    if Answer == 0:
        return (True)


#--------------------------------------------------------

"""
# Checks to see if two numbers are relitively Prime
# Returns a True or False Boolean Statement    
"""

def isrelativeprime(a, b):

    # Function Checks to see if two numbers are relatively Prime
    # returns a True or False Boolean Statement

    if a < 1:
        return ("INVALID INTEGER: Only excepts input of integers higher than 1")


    import stdarray
    import stdio
    import sys

    # creates an array to check the max and min values for looping

    MAXANDMINCHECK = stdarray.create1D(2, 0)
    
    MAXANDMINCHECK[0] = a
    MAXANDMINCHECK[1] = b

    a = max(MAXANDMINCHECK)
    b = min(MAXANDMINCHECK)


    # loops each possible divisor and checks for remainders

    for k in range(2, a):

        # Checks both numbers to see if the indexed number would leave a remainder
        # if they both don't have a remainder, they have a common factor, return false

        if (a % k == 0) and (b % k == 0):
            return False
            break

        #if the counter gets the whole way to the end of the largest number, there
        # are no common factors

        if k == a - 1:
            return True


#---------------------------------------------------------

"""
# returns the factors of an integer
"""


def factors(a):
    
    #create a place to put the final factors

    FactorValues = {}

    import stdarray

    Index = 0

    FactorStorage = stdarray.create1D(a, 0)

    #find the factors

    for i in range(1, a):
        if a % i == 0:
            CurrentNumber = i
            FactorStorage[i] = CurrentNumber

    #take only the factors from the array and place them in the final list

    for k in range(0, len(FactorStorage)):
        if FactorStorage[k] == 0:
            pass
        if FactorStorage[k] !=0:
            FactorValues[Index] = FactorStorage[k]
            Index += 1

    # print the factors

    return FactorValues
    

#----------------------------------------------------------

"""
# Returns the greatest common divisor of two numbers
"""

def divisor(a, b):

    #first check if a perameter is actually the answer
    #return if true

    if a % b == 0:
        return b

    #if not, pass

    if a % b != 0:
        pass 

    #check all the possible answer up to the smaller number of the two

    for c in range(int(b/2), 0, -1):
        if a % c == 0 and b % c == 0:
            Answer = c
            break

    return c

    # squarespace was used to help me form the second half of this


#-----------------------------------------------------------

"""
#returns the least common multiple of two perameters
"""

def multiple(a, b):

    #find out with value is the largest

    import stdarray

    MAXANDMINCHECK = stdarray.create1D(2, 0)
    
    MAXANDMINCHECK[0] = a
    MAXANDMINCHECK[1] = b

    # give "largest" the maximum value

    Largest = max(MAXANDMINCHECK)

    #infinite loop until it reaches the first common multiple

    while True:
        if ((Largest % a == 0) and (Largest % b == 0)):
            Answer = Largest
            break

        Largest += 1

    return Answer

#-------------------------------------------------------

"""
#returns the totient function output for an "n" input
"""

def totient(n):

    #first check to see if n is prime
    
    import stdio

    FactorCounter = 0
    variable = n

    if variable > 1:
        for i in range(2, variable):
            if variable % i != 0:

                # if the number is prime, it has no factors, therefore you
                # can take the variable "n" and subtract 1, giving you the answer

                return n - 1

            if variable % i == 0:

                FactorCounter +=1

                break

    # loops each possible divisor and checks for remainders

    FactorValues = {}
    import stdarray

    Index = 0

    FactorStorage = stdarray.create1D(n, 0)

    #find the factors

    for i in range(1, n):
        if n % i == 0:
            CurrentNumber = i
            FactorStorage[i] = CurrentNumber

    #take only the factors from the array and place them in the final list

    for k in range(0, len(FactorStorage)):
        if FactorStorage[k] == 0:
            pass
        if FactorStorage[k] !=0:
            FactorValues[Index] = FactorStorage[k]
            Index += 1

    #this takes your total number and subtracts all factors from n, 
    #leaving the number of relatively prime numbers (the answer)

    Answer = (n - (len(FactorValues)))


    # compensate for irregularities after 5

    if n > 5:
        Answer = Answer - 1

    return Answer


#---------------------------------------------------------------

"""
# answers the question, is this integer odd? returns True or False
"""

def isodd(a):
    if a % 2 != 0:
        return True
    else:
        return False

#---------------------------------------------------------------

"""
# answers the question, is this integer even? returns True or False
"""

def iseven(a):
    if a % 2 != 0:
        return False
    else:
        return True

#--------------------------------------------------------------
    
    
    
   

def main():

    import sys
    import stdio

    V1 = int(sys.argv[1])
    V2 = int(sys.argv[2])

    

    stdio.writeln("----------------")
    stdio.writeln("isprime Test")
    Answer = isprime(V1)
    stdio.writeln(Answer)
    stdio.writeln("----------------")

    stdio.writeln()
    stdio.writeln()

    stdio.writeln("----------------")
    stdio.writeln("isrelativeprime Test")
    stdio.writeln(isrelativeprime(V1, V2))
    stdio.writeln("----------------")

    stdio.writeln()
    stdio.writeln()

    stdio.writeln("----------------")
    stdio.writeln("factors Test")
    stdio.writeln(factors(V1))
    stdio.writeln("----------------")

    stdio.writeln()
    stdio.writeln()

    stdio.writeln("----------------")
    stdio.writeln("divsor Test")
    stdio.writeln(divisor(V1, V2))
    stdio.writeln("----------------")

    stdio.writeln()
    stdio.writeln()
  
    stdio.writeln("----------------")
    stdio.writeln("multiple Test")
    stdio.writeln(multiple(V1, V2))
    stdio.writeln("----------------")

    stdio.writeln()
    stdio.writeln()

    stdio.writeln("----------------")
    stdio.writeln("totient Test")
    stdio.writeln(totient(V1))
    stdio.writeln("----------------")

    stdio.writeln()
    stdio.writeln()

    stdio.writeln("----------------")
    stdio.writeln("isodd Test")
    stdio.writeln(isodd(V1))
    stdio.writeln("----------------")

    stdio.writeln()
    stdio.writeln()

    stdio.writeln("----------------")
    stdio.writeln("iseven Test")
    stdio.writeln(iseven(V1))
    stdio.writeln("----------------")




if __name__ == '__main__':
    main()