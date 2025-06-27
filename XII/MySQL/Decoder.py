# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 09:07:57 2023

@author: ANKUR
"""


# ENCODE AND DECODE USING BASE64


# importing the module that does this.
import base64

# Decoding the encoded message
encoded = input('Enter the message you want to decode: ')
encoded.strip("'b")
encoded_message = bytes(encoded, 'utf-8')

original_message_decode = base64.b64decode(encoded).decode('utf-8')
# except UnicodeDecodeError:
#     original_message_decode = base64.b64decode(encoded_message)

print('\nDecoded Message:',original_message_decode)
input('Press ENTER to continue...')