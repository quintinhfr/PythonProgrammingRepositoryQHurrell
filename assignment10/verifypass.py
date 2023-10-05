# verifypass.py

import sys
import stdio
import stdarray



def PasswordVerification(Password):

    VerifyCounterCharacters = 0

    VerifyCounterDigits = 0

    VerifyCounterLower = 0

    VerifyCounterUpper = 0

    VerifyCounterOther = 0

    LowerCaseLetters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']

    UpperCaseLetters = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'A', 'I', 'O', 'P', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']

    Digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    CharacterList = list(Password)

    stdio.writeln(CharacterList)

    # - At least 8 characters long

    if len(CharacterList) >= 8:
        VerifyCounterCharacters += 1

    # contains at least 1 digit

    for i in range(len(CharacterList)):

        if CharacterList[i] in Digits:
            VerifyCounterDigits += 1

    # Contains at least 1 uppercase letter

    for j in range(len(CharacterList)):

        if CharacterList[j] in UpperCaseLetters:
            VerifyCounterUpper += 1

    # Contains at least 1 lower case letter

    for k in range(len(CharacterList)):
    
        if CharacterList[k] in LowerCaseLetters:
            VerifyCounterLower += 1

    # Contains at least one character that is not a letter or number

    for q in range(len(CharacterList)):

        if CharacterList[q] not in Digits:
            if CharacterList[q] not in LowerCaseLetters:
                if CharacterList[q] not in UpperCaseLetters:
                    VerifyCounterOther += 1

    # Check to insure that all criteria was met


    if VerifyCounterOther > 0:
        if VerifyCounterDigits > 0:
            if VerifyCounterUpper > 0:
                if VerifyCounterLower > 0:
                    if VerifyCounterCharacters > 0:
                        return True

    # if not return False

    if VerifyCounterOther == 0:
        return False

    if VerifyCounterDigits == 0:
        return False

    if VerifyCounterUpper == 0:
        return False

    if VerifyCounterLower == 0:
        return False

    if VerifyCounterCharacters == 0:
        return False




def main():
    
    Password = str(sys.argv[1])

    Validation = PasswordVerification(Password)

    stdio.writeln(Validation)



if __name__ == '__main__':
    main()
    
    

        
                    
                    
            

        

    
    

    