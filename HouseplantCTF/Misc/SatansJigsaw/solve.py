#! /usr/bin/env python3

import cv2  
import glob
import numpy as np 
from PIL import Image
from pathlib import Path
from pprint import pprint
from natsort import natsorted
from Crypto.Util.number import *

chal_dir = Path('chall')
chal_files = chal_dir.glob('*.jpg')

result_img = Image.new('RGB', (300, 300))

for i in natsorted(chal_files):
    file_name = i.stem
    pprint("### Start:{}".format(file_name))

    pos = long_to_bytes(int(file_name)).decode().split()
    x_pos = int(pos[0])
    y_pos = int(pos[1])
    
    pixel_img = cv2.imread(str(i))
    pixel_rgb = cv2.cvtColor(pixel_img, cv2.COLOR_BGR2RGB) 

    r = int(pixel_rgb[0][0][0])
    g = int(pixel_rgb[0][0][1]) 
    b = int(pixel_rgb[0][0][2])

    result_img.putpixel((x_pos, y_pos), (r,g,b))
    
result_img.save('./result_img.jpg')
result_img.show()

