# binary? - Cryptography
## Information about the challenge
- CTF Name : NexZero 2024
- CTF Organizers : Nexus Club
- Category : Cryptography
- Author : sami_mst
- Points : 50
- Solves : 15/15
- Onsite Players : 15
- Flag Format : nexus{flag}
- Date : 29/02/2024
- Duration : 36 Hours
## Description & Goals
```
i encoded the flag using ones and zeros
```
Also we're given a `flag.txt` file containing this sequence of ones and zeros:
```
10111100111111011100
01110001001
010111101001010
100001010110
0010011000
110101001110011110
1101110101111011
101010
110001
100000111
10111110011010111111
101101101101
010011
011111101100000
11101101101111111010
101110100
10111110100111101011
100100100
110111111110111010010
1101001000
011010
0001100
10110100011110111101
```
Let's go through the thought process.
## Thought Process
When I first encounterd this challenge, my brain went straight to [bacon's cipher](https://en.wikipedia.org/wiki/Bacon%27s_cipher), but the number of bits is 294, it's not a multiplication of 5.

I hated myself for like 3 hours, then i said to myself, the lines aren't even. let's calculate the lengths.
i found this sequence:
```
[20, 11, 15, 12, 10, 18, 16, 6, 6, 9, 20, 12, 6, 15, 20, 9, 20, 9, 20, 10, 6, 7, 20]
```
then i tried to map it to characters in the alphabet:
```python
a = [20, 11, 15, 12, 10, 18, 16, 6, 6, 9, 20, 12, 6, 15, 20, 9, 20, 9, 20, 10, 6, 7, 20]
flag = ""
for c in a:
    flag += chr(ord('a') + c - 1)

print(flag)
```
```
tkoljrpffitlfotititjfgt
```
Meaningless.

But it led to something big. after some thinking and annoying the authors, I calculated the zeros and ones in each line.
I found this:
```
[6, 6, 7, 7, 7, 7, 4, 3, 3, 5, 5, 4, 3, 7, 5, 4, 6, 6, 6, 6, 3, 5, 7]
[14, 5, 8, 5, 3, 11, 12, 3, 3, 4, 15, 8, 3, 8, 15, 5, 14, 3, 15, 4, 3, 2, 13]
```
No value exceeded 15, so it might be a hex value.
let's make it a hex sequence:
```
['6', '6', '7', '7', '7', '7', '4', '3', '3', '5', '5', '4', '3', '7', '5', '4', '6', '6', '6', '6', '3', '5', '7']
['e', '5', '8', '5', '3', 'b', 'c', '3', '3', '4', 'f', '8', '3', '8', 'f', '5', 'e', '3', 'f', '4', '3', '2', 'd']
```
Wait, this looks familiar, let's encode `nexus` in hex:
```
6e 65 78 75 73
```
Yeah that's it, let's just concatinate the two arrays and decode the result:
```
b'nexus{L33T_H3x_Encod3R}'
```
## Solve
```python
with open("crypto/binary/flag.txt", 'r') as file:
    lines = [line.strip() for line in file.readlines()]

ones = []
zeros = []
for i in lines:
    ones.append(i.count('1'))
    zeros.append(i.count('0'))

print(zeros)
print(ones)

hex_str = "".join([hex(zeros[i])[2:] + hex(ones[i])[2:] for i in range(len(ones))])

print(bytes.fromhex(hex_str))
```

## The Flag
```
nexus{L33T_H3x_Encod3R}
```