from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import streamlit as st
import os

@st.cache_data(show_spinner=False)
def decrypt_code(encrypted_file: str, key: bytes):
    # Read the encrypted file
    with open(encrypted_file, "rb") as file:
        ciphertext = file.read()

    # Decrypt the data using AES-256
    cipher = Cipher(
        algorithms.AES(key),
        modes.CFB(os.urandom(16)),  # Ensure the mode matches during encryption
        backend=default_backend()
    )
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()

    return decrypted_data.decode()

# Get the strong key from Streamlit secrets
strong_key = st.secrets["ENCRYPTION_KEY"]

# Path to the encrypted code
encrypted_file_path = "encrypted_code.bin"

try:
    # Decrypt and execute the code
    decrypted_code = decrypt_code(encrypted_file_path, bytes.fromhex(strong_key))
    exec(decrypted_code)
except Exception as e:
    st.error("Error decrypting or executing the code.")
    st.error(str(e))

# Cleanup after execution
decrypted_code = None
