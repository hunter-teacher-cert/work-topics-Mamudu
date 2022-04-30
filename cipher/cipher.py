# Mamudu, Eduardo and Michele worked together

##### Asynch Starts here  #######
def encrypt(text, s):
    result = ""
    # traverse the plain text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters in plain text
        if (char.isupper()):
            #convert the letter into unicode
            #make A unicode 0 by subtracting 65
            #add shift
            #allow wraparound by mod 26
            #make A's unicode 65 again by adding 65
            #convert back from unicode to letter
            result += chr((ord(char) - 65 + s) % 26 + 65)
        # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) - 97 + s) % 26 + 97)
    return result


#enter alphabetic text without spaces and a desired shift
text = "Mamudu"
s = 27

print("Plain Text : " + text)
print("Shift pattern : " + str(s))
print("Cipher: " + encrypt(text, s))
print()


#Hw bellpepper version starts here
def decrypt(text, s):
    result = ""
    # transverse the plain text
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) - 65 - s) % 26 + 65)
        else:
            result += chr((ord(char) - 97 - s) % 26 + 97)
    return result


#### Homework Bell Pepper Version ####### 
# Write a function that decrypts a symmetric cipher with a given shift
text = "Nbnvev"
s = 27

print("Plain Text : " + text)
print("Shift pattern : " + str(s))
print("Cipher: " + decrypt(text, s))