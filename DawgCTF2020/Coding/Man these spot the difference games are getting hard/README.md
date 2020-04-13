# Man these spot the difference games are getting hard
---
## Approach
I got the crypt information and cipher text from server.
So decrypt cipher text and return server.
```
-----------------------------------------------------------------------
Welcome to DiffSpot, a new Spot the Differnce Game sponsored by DawgSec
          You'll be presented with a variety of encoded data,
              all of which will be of the form DogeCTF{}
Possible ciphers include:
- rot13
- rot16
- base64
- base32
- base16
- atbash
- affine with b=6, a=9
- railfence with key=3
         Your job is to decode the flag and send it back to us
                     Seems easy enough right?
-----------------------------------------------------------------------
RG9nZUNURntSbWpsV0lhTllmTHR0c3RYUXVoWUpBa3l2VGx5emtDUn0=
```

## Solution
Using Man_these_solve.py

## Flag
```
DawgCTF{w@iT_th3y_w3r3_d1ff3rent?!}
```