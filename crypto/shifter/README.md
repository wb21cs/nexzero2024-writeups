# SHIFTER - Cryptography
## Information about the challenge
- CTF Name : NexZero 2024
- CTF Organizers : Nexus Club
- Category : Cryptography
- Author : mo_4m1n3
- Points : 50
- Solves : 15/15
- Onsite Players : 15
- Flag Format : nexus{flag}
- Date : 29/02/2024
- Duration : 36 Hours
## Description & Goals
```
Gold Represent Divine Love! add the plaintext found to the flag format nexus{plain_text}
```
Also you're given this IP address:
```
nc nex-zero.nexus-security-club.com 4410
```
## Solve
Let's connect.
```
SHIFTER BY M0/MASSI
Welcome To SHIFTER here your flag encrypted :
 sijhwnvt_wjuj_lwyy_gjdrsipxijjk
------------------------------------------------------------------------------------------------------
Give me Your Text to Encrypt it :
```
Let's try to give it the flag:
```
HERE IS YOUR ENCRYPTED DATA: sjkjzsdg_wkvl_qelt_hkfuxqcsikkm
```
Emmm. it doesn't work.

But wait, we can see that some characters didn't change, like the first `s`. there must be a pattern.

Let's feed it a big sequence of the latter `a`:
```
HERE IS YOUR ENCRYPTED DATA: abbcdfinviabbcdfinviabbcdfinviabbcdfinviab
```
Look there! we found something, this sequence `abbcdfinvi` is repeating itself.

We can reverse it by making a script that checks the index of the letter than shift it back according to the sequence's matching character:
```python
c_map = "abbcdfinv"
cipher = "sijhwnvt_wjuj_lwyy_gjdrsipxijjk"
flag = ""

def shift(c, s):
    return chr((ord(c) - ord('a') + s) % 26 + ord('a'))

for i in range(len(cipher)):
    if cipher[i] == "_":
        flag += "_"
    else:
        flag += shift(cipher[i], ord('a') - ord(c_map[i%9]))

print(flag)
```
```
shifting_with_gold_fibonacciiii
```
We found something meaningful.

Let's wrap it with the flag's header and submit it.

## The Flag
```
nexus{shifting_with_gold_fibonacciiii}
```