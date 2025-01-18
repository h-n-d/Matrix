import streamlit as st
from cryptography.fernet import Fernet

# Load the Fernet key from Streamlit secrets
fernet_key = st.secrets["ENCRYPTION_KEY"]

# Initialize the Fernet cipher
cipher = Fernet(fernet_key)

# Function to decrypt and execute code
def decrypt_and_execute(encrypted_file: str, key: Fernet):
    try:
        # Read the encrypted file
        with open(encrypted_file, "rb") as file:
            encrypted_data = file.read()

        # Decrypt the data in memory
        decrypted_code = key.decrypt(encrypted_data).decode()

        # Execute the decrypted code
        exec(decrypted_code, globals())  # Use globals() to maintain imports/context
    except Exception as e:
        st.error("Error decrypting or executing the code.")
        st.error(str(e))
    finally:
        # Clear decrypted code from memory
        decrypted_code = None

# Path to your encrypted code file
encrypted_file_path = "encrypted_code.bin"

# Decrypt and execute at runtime
decrypt_and_execute(encrypted_file_path, cipher)
