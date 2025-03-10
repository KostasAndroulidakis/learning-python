"""Applies your custom cipher algorithm."""

def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message:
        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:
            # Store original case
            is_upper = char.isupper()
            # Convert to lowercase for processing
            char_lower = char.lower()
            
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char_lower)
            new_index = (index + offset*direction) % len(alphabet)

            # Restore original case
            result_char = alphabet[new_index]
            if is_upper:
                result_char = result_char.upper()
                
            final_message += result_char
    
    return final_message

def encrypt(message, key):
    return vigenere(message, key)
    
def decrypt(message, key):
    return vigenere(message, key, -1)