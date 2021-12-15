def superDigit(stringN, PconcatofN):    
    bigDigitStr = PconcatofN * stringN
    digit = int(bigDigitStr)
    return recurseCall(digit)

def recurseCall(digit):
    if len(str(digit)) == 1:
        return digit
    numCharList = list(str(digit))
    sum = 0
    for a in numCharList:
        sum += int(a)   
    return recurseCall(str(sum))


print(superDigit("148", 3))