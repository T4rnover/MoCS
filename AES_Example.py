from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import base64

# Read plain text
plain_text = input("Enter the plain text: ")

# Prompt for a key
key = input("Enter the encryption key (16 characters): ")
assert len(key) == 16, "Key must be 16 characters"

# Convert key and plain text to bytes
key = key.encode()
plain_text = plain_text.encode()

# Generate a random initialization vector
iv = get_random_bytes(16)

# Create a new AES cipher object
cipher = AES.new(key, AES.MODE_CBC, iv)

# Encrypt the plain text
encrypted_text = cipher.encrypt(pad(plain_text, AES.block_size))

# Print the plain text and encrypted text
print("Plain text:", plain_text.decode())
print("Encrypted text:", base64.b64encode(iv + encrypted_text).decode())