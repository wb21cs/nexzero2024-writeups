cipher = 'lo o lool ool ooo { oloo lllll oloo _ l oooo ooool l _ oll ooool ooo _ ll lll olo ooo oooll _ ooool oolo l oooll olo _ ooool oloo oloo }'
flag = ''
for c in cipher:
    if c == 'l':
        flag += '_'
    elif c == 'o':
        flag += '.'
    elif c != '_':
        flag += c

print(flag)

# pass it to dcode and put back the seprators

flag = 'NEXUS{L0L_TH4T_W4S_MORS3_4FT3R_4LL}'
print(flag.lower())