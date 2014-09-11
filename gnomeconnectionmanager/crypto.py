"""
This module contains the encryption and the decryption routines for the gnome
connection manager.
"""

import pyAES
import base64

def encrypt(passw, string):
    try:
        s = pyAES.encrypt(string, passw)
    except:
        s = ""
    return s
    
def decrypt(passw, string):
    try:
        s = decrypt_old(passw, string) if conf.VERSION == 0 else pyAES.decrypt(string, passw)
    except:
        s = ""
    return s

def decrypt_old(passw, string):
    try:
        ret = xor(passw, base64.b64decode(string))
        s = "".join(ret)
    except:
        s = ""
    return s
    
def encrypt_old(passw, string):
    try:
        ret = xor(passw, string)    
        s = base64.b64encode("".join(ret))
    except:
        s = ""
    return s

