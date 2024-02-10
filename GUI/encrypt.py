import os
import shutil
from cryptography.fernet import Fernet
# hello
class FileEncryptorDecryptor:
    def __init__(self, key):
        self.key = key
        self.cipher = Fernet(key)

    def encrypt_file(self, input_file, output_file):
        # Encrypts a single file using the provided key
        with open(input_file, 'rb') as f:
            data = f.read()
            encrypted_data = self.cipher.encrypt(data)
        with open(output_file, 'wb') as f:
            f.write(encrypted_data)

    def decrypt_file(self, input_file, output_file):
        # Decrypts a single file using the provided key
        with open(input_file, 'rb') as f:
            data = f.read()
            decrypted_data = self.cipher.decrypt(data)
        with open(output_file, 'wb') as f:
            f.write(decrypted_data)

    def batch_encrypt_files(self, input_dir, output_dir):
        # Encrypts multiple files in a directory
        for filename in os.listdir(input_dir):
            if os.path.isfile(os.path.join(input_dir, filename)):
                input_file = os.path.join(input_dir, filename)
                output_file = os.path.join(output_dir, filename + '.encrypted')
                self.encrypt_file(input_file, output_file)

    def batch_decrypt_files(self, input_dir, output_dir):
        # Decrypts multiple files in a directory
        for filename in os.listdir(input_dir):
            if os.path.isfile(os.path.join(input_dir, filename)):
                input_file = os.path.join(input_dir, filename)
                output_file = os.path.join(output_dir, filename[:-10])  # remove '.encrypted' from filename
                self.decrypt_file(input_file, output_file)

    def shred_file(self, file_path):
        # Securely deletes a file by overwriting it with random data before deletion
        with open(file_path, 'rb+') as f:
            length = f.tell()
            f.seek(0)
            f.write(os.urandom(length))
        os.remove(file_path)

    # Additional methods for UI integration, error handling, logging, etc. can be added here

# Main function for CLI usage
def main():
    key = Fernet.generate_key()  # Generate a random encryption key
    encryptor_decryptor = FileEncryptorDecryptor(key)

    # Example usage:
    input_file = 'example.txt'
    encrypted_file = 'example.txt.encrypted'
    decrypted_file = 'example_decrypted.txt'
    encryptor_decryptor.encrypt_file(input_file, encrypted_file)
    encryptor_decryptor.decrypt_file(encrypted_file, decrypted_file)

    input_dir = 'input_directory'
    output_dir = 'output_directory'
    encryptor_decryptor.batch_encrypt_files(input_dir, output_dir)
    encryptor_decryptor.batch_decrypt_files(output_dir, input_dir)

    file_to_shred = 'file_to_shred.txt'
    encryptor_decryptor.shred_file(file_to_shred)

if __name__ == "__main__":
    main()
