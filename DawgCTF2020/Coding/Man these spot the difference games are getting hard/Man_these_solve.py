from pwn import *
import math
import sys
import string
import codecs
import subprocess
from pycipher import Atbash, Affine, Railfence
from pprint import pprint

HOST = 'ctf.umbccd.io'
PORT = 5200


# from https://www.geeksforgeeks.org/rail-fence-cipher-encryption-decryption/
def decryptRailFence(cipher, key): 
  
    # create the matrix to cipher  
    # plain text key = rows ,  
    # length(text) = columns 
    # filling the rail matrix to  
    # distinguish filled spaces 
    # from blank ones 
    rail = [['\n' for i in range(len(cipher))]  
                  for j in range(key)] 
      
    # to find the direction 
    dir_down = None
    row, col = 0, 0
      
    # mark the places with '*' 
    for i in range(len(cipher)): 
        if row == 0: 
            dir_down = True
        if row == key - 1: 
            dir_down = False
          
        # place the marker 
        rail[row][col] = '*'
        col += 1
          
        # find the next row  
        # using direction flag 
        if dir_down: 
            row += 1
        else: 
            row -= 1
              
    # now we can construct the  
    # fill the rail matrix 
    index = 0
    for i in range(key): 
        for j in range(len(cipher)): 
            if ((rail[i][j] == '*') and
               (index < len(cipher))): 
                rail[i][j] = cipher[index] 
                index += 1
          
    # now read the matrix in  
    # zig-zag manner to construct 
    # the resultant text 
    result = [] 
    row, col = 0, 0
    for i in range(len(cipher)): 
          
        # check the direction of flow 
        if row == 0: 
            dir_down = True
        if row == key-1: 
            dir_down = False
              
        # place the marker 
        if (rail[row][col] != '*'): 
            result.append(rail[row][col]) 
            col += 1
              
        # find the next row using 
        # direction flag 
        if dir_down: 
            row += 1
        else: 
            row -= 1
    return("".join(result)) 


    
def check(text):
    return True if 'DogeCTF' in text or 'DOGECTF' in text else False

if __name__ == '__main__':
    io = remote(HOST, PORT)
 
    rot13 = str.maketrans( "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
    atbash =str.maketrans( "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", "ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba")

    # affine value
    a = 9
    b = 6

    #Railfence key
    k = 3

    desc = io.recvuntil('right?')
    bar = io.recvuntil('-----------------------------------------------------------------------\n')

    for i in range(0,1000):
        tmp = ''
        ans = ''
        try:
            cipher_string = io.recvline().decode().rstrip('\n')
        except:
            print(io.recv())
        
        print("Cipher Sting:{}".format(cipher_string))
        
        #base16
        try:
            tmp = base64.b16decode(cipher_string).decode()
            if check(tmp):
                ans = tmp
        except:
            print("### Not base16 ###")
        
        #base32
        try:
            tmp = base64.b32decode(cipher_string).decode()
            if check(tmp):
                ans = tmp
        except:
            print("### Not base32 ###")
        
        #base64
        try:
            tmp = base64.b64decode(cipher_string).decode()
            if check(tmp):
                ans = tmp
        except:
            print("### Not Base64 ####")
        
        #rot13
        try:
            tmp = str.translate(cipher_string, rot13)
            if check(tmp):
                ans = tmp
        except:
            print("### Not rot13 ###")
    
        #rot16
        try:
            decode_rot16_cmd = "echo {} | tr ‘q-za-pQ-ZA-P’ ‘a-zA-Z’".format(cipher_string)
            res = subprocess.run(decode_rot16_cmd, stdout=subprocess.PIPE,  shell=True)
            tmp = res.stdout.decode().rstrip('\n')
            if check(tmp):
                ans = tmp
        except:
            print("### Not rot16 ###")

        #atbash 
        try:
            tmp = str.translate(cipher_string, atbash)
            if check(tmp):
                ans = tmp
        except:
            print("### Not atbash ###")
        
        #affine
        try:
            tmp = Affine(a, b).decipher(cipher_string)
            if "DOGECTF" in tmp:
                tmp = tmp[0:7] + '{' + tmp[7:] + '}'
                if check(tmp):
                    ans = tmp
            
        except:
            print("### Not affine ###")

        #railfence
        try:
            tmp = decryptRailFence(cipher_string, k)
            if check(tmp):
                ans = tmp
        except:
            print("### Not affine ###") 

        print("ANSER:{}".format(ans))
        io.sendline(str(ans))
        
        