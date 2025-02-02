from cryptography.fernet import Fernet
import base64

#generamos una clave

key= Fernet.generate_key()
cipher_suite = Fernet(key)

#funcion cifrado de datos

def encrypt_message(message):
    cipher_text = cipher_suite.encrypt(message.encode())
    return base64.urlsafe_b64encode(cipher_text).decode()

#Funcion para decifrar datos

def decrypt_message(cipher_text):
    decode_cipher_text = base64.urlsafe_b64decode(cipher_text)
    decrypyed_message = cipher_suite.decrypt(decode_cipher_text).decode()
    return decrypt_message