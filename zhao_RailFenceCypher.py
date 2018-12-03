'''
Railfence cypher written by William 
Help from @profecali on youtube
'''
def encrypt(plainText):
    evenChars = ''
    oddChars= ''

    charCount = 0
    for ch in plainText:
        if charCount % 2 is 0:
            evenChars = evenChars + ch
        else:
            oddChars = oddChars + ch

        charCount = charCount + 1
    cipherText = oddChars + evenChars
    return cipherText

msg = encrypt(input('Please enter a message that you would desire to encrypt: '))
print(msg)

 
    

def decrypt(cipherText):
    halfLength = len(cipherText) // 2
    evenChars = cipherText[halfLength:]
    oddChars = cipherText[:halfLength]
    plainText = ''
    for i in range(halfLength):
        plainText = plainText + evenChars[i]
        plainText = plainText + oddChars[i]

    if len(evenChars) > len(oddChars):
        plainText = plainText + evenChars[-1]
    return plainText

plain= decrypt(msg)

print(plain)
    