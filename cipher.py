def caesar_cipher(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += char
    return result

# Example usage:
text = "Mohsin Ahmed"
shift = 3
encrypted_text = caesar_cipher(text, shift)
print("Encrypted text:", encrypted_text)

# Decrypting
decrypted_text = caesar_cipher(encrypted_text, -shift)
print("Decrypted text:", decrypted_text)