# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 09:57:12 2023

@author: ANKUR
"""

while True:    
    print('\n\n------------------------------')
    print('Encode or Decode your STRINGS:')
    print('\n1: Encode')
    print('2: Decode')
    print('0: Exit')
    ch = int(input('\nEnter your choice: '))
    
    
    if ch ==1 :
        # importing the module that does this.
        import base64

        # Encoding the utf-8 message.
        message = input('\nEnter the message you want to encode: ')
        message = bytes(message, 'utf-8')
        encoded_message = base64.b64encode(message)
        mess = str(encoded_message)
        print('\nEncoded Message:',encoded_message)
        input('\nPress ENTER to continue...')
    
    elif ch == 2:
        import base64

        # Decoding the encoded message
        encoded = input('\nEnter the message you want to decode: ')
        encoded.strip("'b")
        encoded_message = bytes(encoded, 'utf-8')

        original_message_decode = base64.b64decode(encoded).decode('utf-8')
        # except UnicodeDecodeError:
        #     original_message_decode = base64.b64decode(encoded_message)

        print('\nDecoded Message:',original_message_decode)
        input('\nPress ENTER to continue...')
    
    elif ch == 0:
        print('\n\nThank You...')
        print('Bye')
        break
    
    else:
        print('Invalid input...')
        input('Press ENTER to continue...')