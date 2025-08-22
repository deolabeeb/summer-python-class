# The text we want to decrypt (already encrypted using the Vigenère cipher)
text = 'mrttaqrhknsw ih puggrur'

# The custom key used for encryption/decryption
custom_key = 'happycoding'


# Function to perform the Vigenère cipher
def vigenere(message, key, direction=1):
    # Keeps track of which character in the key we are on
    key_index = 0

    # Define the alphabet used for encryption/decryption
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # Store the final encrypted or decrypted result
    final_message = ''

    # Loop through each character in the message (convert to lowercase first)
    for char in message.lower():

        # If the character is NOT a letter (like space, punctuation), keep it as it is
        if not char.isalpha():
            final_message += char
        else:
            # Pick the correct key character based on key_index (loop around if needed)
            key_char = key[key_index % len(key)]
            key_index += 1   # Move to next key character for the next round

            # Find the position (offset) of the key character in the alphabet
            offset = alphabet.index(key_char)

            # Find the index of the current character in the alphabet
            index = alphabet.find(char)

            # Compute new index:
            #   - For encryption: move forward by offset
            #   - For decryption: move backward by offset (direction = -1)
            new_index = (index + offset * direction) % len(alphabet)

            # Add the new encrypted/decrypted character to the final message
            final_message += alphabet[new_index]
    
    # Return the fully encoded/decoded message
    return final_message


# Wrapper function to encrypt using Vigenère (direction = +1)
def encrypt(message, key):
    return vigenere(message, key)


# Wrapper function to decrypt using Vigenère (direction = -1)
def decrypt(message, key):
    return vigenere(message, key, -1)


# --- Execution Part ---

# Print the encrypted message and key
print(f'\nEncrypted text: {text}')
print(f'Key: {custom_key}')

# Decrypt the text with the provided key
decryption = decrypt(text, custom_key)

# Print the decrypted message
print(f'\nDecrypted text: {decryption}\n')