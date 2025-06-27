# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 08:54:05 2023

@author: ANKUR
"""

# ENCODE AND DECODE USING BASE64


# importing the module that does this.
import base64

# Encoding the utf-8 message.
message = input('Enter the message you want to encode: ')
message = bytes(message, 'utf-8')
encoded_message = base64.b64encode(message)
mess = str(encoded_message)
print('\nEncoded Message:',encoded_message)
input('Press ENTER to continue...')