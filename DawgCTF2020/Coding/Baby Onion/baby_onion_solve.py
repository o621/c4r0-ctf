#! /usr/bin/env python3

import os
import sys
import base64
import subprocess
from pathlib import Path
from pprint import pprint

if __name__ == "__main__":
    
    decode_b16_cmd = "cat ./baby.onion | base16 -d > b64_str"
    subprocess.run(decode_b16_cmd, stdout=subprocess.PIPE,  shell=True)
    while(True):
        db64cmd = "cat ./b64_str | base64 -d > b16_str"
        cat_b16file = "cat ./b16_str"
        subprocess.run(db64cmd, stdout=subprocess.PIPE,  shell=True)
        b16 = subprocess.run(cat_b16file, stdout=subprocess.PIPE,  shell=True)
        decode_str = b16.stdout.decode()
    
        if "CTF" in decode_str:
            print("Find flag:{}".format(decode_str))
            break

        db16cmd = "cat ./b16_str | base16 -d > b64_str"
        cat_b64file = "cat ./b64_str"
        subprocess.run(db16cmd, stdout=subprocess.PIPE,  shell=True)
        b64 = subprocess.run(cat_b64file, stdout=subprocess.PIPE,  shell=True)
        decode_str = b64.stdout.decode()
        
        if "CTF" in decode_str:
            print("Find flag:{}".format(decode_str))
            break



