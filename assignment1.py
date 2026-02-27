
key = 'abcdefghijklmnopqrstuvwxyz' # alphabetic key
plaintext = "My name is Manahil Kamran!" # original text

# for encryption:
def enc_caesar(plaintext, shift):  # Function for encryption

    result = ''  # empty string to store encrypted text

    for l in plaintext:  # go through each character

        if l.isalpha():  # check if character is a letter

            if l.islower(): # if lowercase letter

                i = (key.index(l) + shift) % 26 # find position and shift

                result += key[i] # add shifted letter

            else:  # if uppercase letter

                i = (key.index(l.lower()) + shift) % 26 # shift using lowercase index

                result += key[i].upper() # convert back to uppercase
        else:
            result += l  # keep spaces/punctuation unchanged

    return result # return encrypted text

ciphertext = enc_caesar(plaintext, 3)# Encrypt the plaintext with a shift of 3

# for decryption:
def dec_caesar(ciphertext, shift): # Function for decryption

    result = ''  # empty string to store decrypted text

    for l in ciphertext: # go through each character

        if l.isalpha(): # check if character is a letter

            if l.islower(): # if lowercase letter

                i = (key.index(l) - shift) % 26  # shift backwards

                result += key[i] # add original letter

            else:  # if uppercase letter

                i = (key.index(l.lower()) - shift) % 26 # shift backwards using lowercase index

                result += key[i].upper() # convert back to uppercase
        else:
            result += l  # keep spaces/punctuation unchanged

    return result  # return decrypted text

decrypted = dec_caesar(ciphertext, 3) # Decrypt the ciphertext with the shift of 3

# Print results
print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted:", decrypted)