# Base64 - Cryptography
## Information about the challenge
- CTF Name : NexZero 2024
- CTF Organizers : Nexus Club
- Category : Cryptography
- Author : 0utc4st
- Points : 108
- Solves : 15/15
- Onsite Players : 15
- Flag Format : nexus{flag}
- Date : 29/02/2024
- Duration : 36 Hours
## Description & Goals

    Come, i'll take you back to World War 1

    PS: convert the result to lowercase.

And were given this string in a text file named `LOL.txt` 
```
lo o lool ool ooo { oloo lllll oloo _ l oooo ooool l _ oll ooool ooo _ ll lll olo ooo oooll _ ooool oolo l oooll olo _ ooool oloo oloo }
```
Our goal is to extract the flag from this string using the information we're given.

## Solve
As we can see, the ciphertext is constructed using binary values which are `l` and `o`, separated by the separators `{`, `}` and `_`, which makes it look just like the flag we're looking for, so this must be just some kind of encoding using two values only.

Two values encoding? World War 1? this makes me think about ... [Morse Code!](https://en.wikipedia.org/wiki/Morse_code)

We'll convert `l` and `o` into `_` and `.` and removing all the original `_`'s (because it will mess up the decoding) with this python script:
```python
cipher = 'lo o lool ool ooo { oloo lllll oloo _ l oooo ooool l _ oll ooool ooo _ ll lll olo ooo oooll _ ooool oolo l oooll olo _ ooool oloo oloo }'
morse_code = ''
for c in cipher:
    if c == 'l':
        morse_code += '_'
    elif c == 'o':
        morse_code += '.'
    elif c != '_':
        morse_code += c
```
We will get this:
```
_. . _.._ .._ ... { ._.. _____ ._..  _ .... ...._ _  .__ ...._ ...  __ ___ ._. ... ...__  ...._ .._. _ ...__ ._.  ...._ ._.. ._.. }
```
Then we will pass it into [dcode](https://www.dcode.fr/morse-code) to convert the string back into its original form, we will get something like this:

    NEXUSL0LTH4TW4SMORS34FT3R4LL
This is more readable, yeah?

Now we will just put back the separators and make it lowercase.
## The Flag
```
nexus{l0l_th4t_w4s_mors3_4ft3r_4ll}
```