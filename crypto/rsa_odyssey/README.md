# RSA_Odyssey - Cryptography
## Information about the challenge
- CTF Name : NexZero 2024
- CTF Organizers : Nexus Club
- Category : Cryptography
- Author : M3551
- Points : 50
- Solves : 10/15
- Onsite Players : 15
- Flag Format : nexus{flag}
- Date : 29/02/2024
- Duration : 36 Hours

## Description & Goal
```
I've encrypted a flag using RSA, confident in its unbreakable security. But can you prove me wrong?
```
also you're given this ip address:
```
nc nex-zero.nexus-security-club.com 4404
```
## Solve
### Thought process
Let's connect to the server.
We will get this output:
```
n =  7125640909396906186138274925150497663124661893060184035246647334950732476738819362930401387750729175184801633507356865829007494141801270082312736084218253
e =  65537
c =  1663436719558396865345667453776188854717927509627765081608096653294505454111845172743310384821623360597414506949000266176079425776633421465045977957484518
Enter your ciphertext de decrypt it  : 
```
So basically, it gives us the public key and the ciphertext. also it's looking for a ciphertext from us and it will give us its plaintext, it's an oracle challenge. Interesting ...
Let's try their own ciphertext:
```
Enter your ciphertext de decrypt it  : 
1663436719558396865345667453776188854717927509627765081608096653294505454111845172743310384821623360597414506949000266176079425776633421465045977957484518
Unauthorized!!!!!!!!
Enter your ciphertext de decrypt it  : 
```
Unauthorized. hmmm ...
so that ciphertext is blacklisted.

What can we do? let's learn more about RSA's properties ... maybe [homomorphism](https://www.youtube.com/watch?v=r8psTgL4K4M).

So we can send a modified version of the ciphertext that the oracle can't recognize, then we will get our modified plaintext and convert it back to its original form.
let's use `2^e * c`, it will become `2 * plaintext` after decryption. then we will just divide by 2.

```python
n = 7125640909396906186138274925150497663124661893060184035246647334950732476738819362930401387750729175184801633507356865829007494141801270082312736084218253
e = 65537
ct = 1663436719558396865345667453776188854717927509627765081608096653294505454111845172743310384821623360597414506949000266176079425776633421465045977957484518

new_ct = (pow(2, e, n) * ct) % n
print(new_ct)
```
```
6214036480751963788037423383829358592923771124355205800583605819153169574478263319887195873637972940444438871427056893072601837757900417887398233483446868
```
Let's pass this to the oracle:
```
Enter your ciphertext de decrypt it  : 
6214036480751963788037423383829358592923771124355205800583605819153169574478263319887195873637972940444438871427056893072601837757900417887398233483446868
The plaintext is : 120732269388235565081909269023860253883156127861042653728156281869467283543520872930218591020878817018
b'\xdc\xca\xf0\xea\xe6\xf6\x90`\xda`\xda`\xe4\xe0\xd0b\xe6\xda\xbeh\xdc\xc8\xbe\x86\xe4\xf2\xe0n`\xbeh\xe4f\xbeh\xeef\xe6`\xdaf\xfa'
```
it gave us something. let's convert it into an integer and divide it by two, then decode it again:
```python
flag = b'\xdc\xca\xf0\xea\xe6\xf6\x90`\xda`\xda`\xe4\xe0\xd0b\xe6\xda\xbeh\xdc\xc8\xbe\x86\xe4\xf2\xe0n`\xbeh\xe4f\xbeh\xeef\xe6`\xdaf\xfa'
print(bytes.fromhex(hex(int(flag.hex(), 16)//2)[2:]))
```
```
b'nexus{H0m0m0rph1sm_4nd_Cryp70_4r3_4w3s0m3}'
```
And here we go, here is the flag!

## The Flag
```
nexus{H0m0m0rph1sm_4nd_Cryp70_4r3_4w3s0m3}
```