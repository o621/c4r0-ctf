#  Rivest Shamir Adleman 
## Challenge
A while back I wrote a Python implementation of RSA, but Python's really slow at maths. Especially generating primes.

Dev: Tom
 Hint! There are two possible ways to get the flag ;-)
 chall.7z 


## Approach
I checked encrypt.py, decrypt.py and public-key.json and found out private-key.json is neccesary when I used decrypt.py. 
private-key.json must contain **n** and **d**. So I tried to get d.

## Solution
I found http://factordb.com/ and got **p** , **q** from **n**. 
```
p = 58754030774905986805754122995310081662217884210168479550129875193424398870745444673926050610118197084042202162420044553461740174815697964254570199939394803548997633592060223756279974260864378745120001533514186672141428133398599326104981445779780014073764199910798520251506148673445046102194538255507437319319
q = 88761620475672281797897005732643499821690688597370440945258776182910533850401433150065043871978311565287949564292158396906865512113015114468175188982916489347656271125993359554057983487741599275948833820107889167078943493772101668339096372868672343763810610724807588466294391846588859523658456534735572626377
```
You know you could get **d** from **n**, **p**, **q**.
(Let's try https://www.cryptool.org/de/cto-highlights/rsa-schritt-fuer-schritt)
## Flag
```
 .--.
/.-. '----------.
\'-' .--"--""-"-'
 '--'

rtcp{f1xed_pr*me-0r_low_e?}
```