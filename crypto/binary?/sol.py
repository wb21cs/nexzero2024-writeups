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
print(hex_str)

print(bytes.fromhex(hex_str))
