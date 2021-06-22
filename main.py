#source: https://www.101computing.net/random-password-generator/
import random

def getUpperCaseLetter():
    return chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)

def getLowerCaseLetter():
    return chr(random.randint(97, 122))  # Generate a random Lowercase letter (based on ASCII code)

def getDigit():
    return chr(random.randint(48,57))

def getSymbol():
    retval = list()
    range1 = chr(random.randint(33, 47))
    range2 = chr(random.randint(58, 64))
    range3 = chr(random.randint(91, 96))
    range4 = chr(random.randint(123, 126))
    range5 = chr(random.randint(145, 152))
    retval.append(range1)
    retval.append(range2)
    retval.append(range3)
    retval.append(range4)
    retval.append(range5)
    retval.append("€")
    retval.append("£")
    retval.append("¥")
    retval.append("$")
    retval.append("©")
    retval.append("™")
    retval.append("°")
    retval.append("˜")
    retval.append("¡")
    retval.append("¿")
    randIndex = random.randint(0, len(retval)-1)
    return retval[randIndex]

#A function do shuffle all the characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

def formPassword(up, low, dig, sym):
    password = ""
    for i in range(0, up):
        newUpperCaseLetter = getUpperCaseLetter()
        password += newUpperCaseLetter
    for i in range(0, low):
        newLowerCaseLetter = getLowerCaseLetter()
        password += newLowerCaseLetter
    for i in range(0, dig):
        newDigit = getDigit()
        password += newDigit
    for i in range(0, sym):
        newSymbol = getSymbol()
        password += newSymbol
    return password


# Defining main function
def main():
    print("Hello user!")
    print("Welcome to the Random Password Generator!")
    numUpper = int(input("How many uppercase letters do you need? "))
    numLower = int(input("How many lowercase letters do you need? "))
    numDigit = int(input("How many digits do you need? "))
    numSymbols = int(input("How many symbols do you need? "))
    unShuffledPW = formPassword(numUpper, numLower, numDigit, numSymbols)
    password = shuffle(unShuffledPW)
    print("Your new password is: " + password)


# Using the special variable __name__

if __name__ == "__main__":
    main()