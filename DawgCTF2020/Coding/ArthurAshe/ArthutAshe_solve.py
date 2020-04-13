#! /usr/bin/env python3

from pwn import *
import math
import sys
from pprint import pprint

HOST = 'arthurashe.ctf.umbccd.io'
PORT = 8411

def score_checker(gtype, p1, p2):
    return 0 if int(p1) > int(p2) else 1 

if __name__ == '__main__':

    io = remote(HOST, PORT)
    io.sendline('y')
    ans_binary = ''
    for i in range(0,1000):
        try:
            r = io.recvuntil('this ')
        except:
            print("ANS_BINARY:{}".format(ans_binary))
            print(io.recv())
            
        game_type = io.recvuntil(' ').decode('utf-8')
        skip_str = io.recvuntil('is ')

        all_score = io.recvuntil('.').decode('utf-8')[:-1]

        if 'love' in all_score:
            all_score = all_score.replace('love', '0')
        if 'set' in all_score:
            all_score = all_score.replace('set', '60')
        if 'game' in all_score:
            all_score = all_score.replace('game', '75') 
        p1, p2 = all_score.split('-')
        print("Type:{} Score:{} Left:{} Right:{}".format(game_type, all_score, p1, p2))
        ans = score_checker(game_type, p1, p2)
        print("Ans:{}".format(ans))
        ans_binary += str(ans)
        io.sendline(str(ans))
        