KEYLOGGER PROJECT

This is a simple keylogger script implemented in Python that captures keystrokes, saves them to a log file, and encrypts the log for added security. The script uses the pynput library to listen to keyboard events and the cryptography library to encrypt the logs.

Features
Keylogging: Captures each keystroke made by the user.
Encryption: Encrypts the log file to ensure the data is protected.
Log File: The captured keys are written to a log file (key_log.txt).
Keylogger Status: The script outputs status messages in the terminal to notify the user of its actions (e.g., when it starts and stops).
Esc to Stop: The keylogger can be stopped by pressing the Esc key.
Requirements
Python 3.x
Required Python packages:
pynput
cryptography
You can install the required packages using pip:

-> pip install pynput cryptograhpy

################# SETUP ############################################
1.Generate a Key: When the script is first run, it will generate a key and store it in a file called key.key. This key is used to encrypt the log file. If the key already exists, it will simply load the existing key.

2.Log File: All captured keystrokes are logged in a file called key_log.txt. When the script finishes running (by pressing Esc), the log file will be encrypted using the generated key.

################## HOW TO USE ######################################

1.Clone or download the repository.

2. Run the script:
   - python key.py

3.The keylogger will start capturing keystrokes and save them to key_log.txt.

4.Press Esc to stop the keylogger. The log file will be encrypted after stopping.

################### EXAMPLE OUTPUT ###########################################

When the script is running, the terminal will show messages like:

###############################################################
#                                                             #
#                  KEYLOGGER STARTED                         #
#                                                             #
#     Press 'Esc' to stop and encrypt the log                  #
#                                                             #
###############################################################

[INFO] Keylogger is running and capturing keystrokes...
[INFO] The keystrokes will be logged into the log file.
[INFO] Press 'Esc' to stop and encrypt the log.

After pressing Esc to stop the keylogger, the terminal will show:

###############################################################
#                                                             #
#                 KEYLOGGER STOPPED                          #
#                                                             #
#      The log has been encrypted successfully!                #
###############################################################

############# LEGAL DISCLAIMER ##############################
This tool is intended for educational purposes only. Do not use this keylogger on any system without explicit permission from the system's owner. Unauthorized use of keyloggers is illegal in many jurisdictions and can lead to severe consequences.





