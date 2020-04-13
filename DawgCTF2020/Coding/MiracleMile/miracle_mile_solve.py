from pwn import *
import math
import sys
from pprint import pprint

HOST = 'ctf.umbccd.io'
PORT = 5300

io = remote(HOST, PORT)

for i in range(0,1000):
    try:
        r = io.recvuntil('ran ')
    except:
        print(io.recv())
    mile = io.recvuntil(' ').decode('utf-8')
    tmp = io.recvuntil('in ')
    hours, minutes, seconds = io.recvuntil(' ').decode('utf-8').split(':')
    total_seconds = (int(hours) * 3600) + (int(minutes) * 60) + int(seconds)
    seconds_per_mile = float(total_seconds) / float(mile)
    minutes_per_mile = int(seconds_per_mile / 60)
    seconds_remainder = int(seconds_per_mile - (minutes_per_mile * 60))
    ans = '{}:{:0=2d}'.format(minutes_per_mile, seconds_remainder)
    rest = io.recv()  
    print(rest)
    print('ans:{}'.format(ans))
    io.sendline(ans)
