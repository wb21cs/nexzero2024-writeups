# Base64 - Cryptography
## Information about the challenge
- CTF Name : NexZero 2024
- CTF Organizers : Nexus Club
- Category : Cryptography
- Author : sami_mst
- Points : 50
- Solves : 10/15
- Onsite Players : 15
- Flag Format : nexus{flag}
- Date : 29/02/2024
- Duration : 36 Hours
## Description & Goal
We're given this string:
```bmV4dXN7YzBOZ1I0VCRfZm9yX2QzQ29kSW5HX3RIMSR9Cg==```.

Your goal is to extract the flag.
## Solve
based on the name and the way string is written we can predict that the flag has been encoded in base 64.

we can use any online tool like [cyberchef](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)&input=Ym1WNGRYTjdZekJPWjFJMFZDUmZabTl5WDJRelEyOWtTVzVIWDNSSU1TUjlDZz09YGBg) or [dcode](https://www.dcode.fr/base-64-encoding) to decode it.

or you can make you own script like this:
```python
import base64

ct = 'bmV4dXN7YzBOZ1I0VCRfZm9yX2QzQ29kSW5HX3RIMSR9Cg==```'

print(base64.b64decode(ct).decode())
```
## The Flag
```
nexus{c0NgR4T$_for_d3CodInG_tH1$}
```