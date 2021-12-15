import numpy as np
from timeit import default_timer as timer
def encryptingFunction(text, key):
    textMatrix = np.zeros([key, len(text)], dtype = str)
    indexCount = 0
    while indexCount < len(text):        
        for a in range(key):
            if indexCount == len(text):
                break            
            textMatrix[a][indexCount] = text[indexCount]
            indexCount += 1  

    encryptedText = ""       
    for a in range(key):
        indexCount = a
        while indexCount < len(text): 
            if indexCount == len(text):
                break
            if textMatrix[a][indexCount]:
                encryptedText += textMatrix[a][indexCount]     
                indexCount += key 

    return encryptedText

def decryptingFunction(text, key):
    textMatrix = np.zeros([key, len(text)], dtype = str)
    stringCount = 0
    for a in range(key):
        indexCount = a        
        while indexCount < len(text): 
            if indexCount == len(text):
                break
            if textMatrix[a][indexCount] == '':
                textMatrix[a][indexCount] = text[stringCount]     
                indexCount += key
                stringCount += 1    

    decryptedText = ""
    indexCount = 0
    while indexCount < len(text):        
        for a in range(key):
            if indexCount == len(text):
                break            
            decryptedText += textMatrix[a][indexCount]
            indexCount += 1 

    return decryptedText


print(encryptingFunction("plain text", 2))
print(decryptingFunction("pantxli et", 2))

start = timer()
secrettext = encryptingFunction("plain text", 2)
end = timer()
print(end - start)

start = timer()
opentext = encryptingFunction("plain text", 3)
end = timer()
print(end - start)


