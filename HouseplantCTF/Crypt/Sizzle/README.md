#  Sizzle

## Challenge
Due to the COVID-19 outbreak, we ran all out of bacon, so we had to use up the old stuff instead. Sorry for any inconvenience caused...
Dev: William
 Hint! Wrap your flag with rtcp{}, use all lowercase, and separate words with underscores.
 Hint! Is this really what you think it is?



## Approach
This is .... morse code?
```
....- ..... ...-. .--.- .--.. ....- -..-- -..-. ..--. -.... .-... .-.-. .-.-. ..-.. ...-- ..... .--.. ...-- .-.-- .--.- -.... -...- .-... ..-.- .-... ..-.. ...--
```

## Solution
No. All units have 5-length so I found out that is [Bacon Cipher](https://en.wikipedia.org/wiki/Bacon%27s_cipher).
```
....- ..... ...-. .--.- .--.. ....- -..-- -..-. ..--. -.... .-... .-.-. .-.-. ..-.. ...-- ..... .--.. ...-- .-.-- .--.- -.... -...- .-... ..-.- .-... ..-.. ...--
00001 00000 00010 01101 01100 00001 10011 10010 00110 10000 01000 01010 01010 00100 00011 00000 01100 00011 01011 01101 10000 10001 01000 00101 01000 00100 00011
```

## Flag
```
rtcp{bacon_but_grilled_and_morsified}
```