import subprocess

hashcode = 0x21DD09EC
a = hashcode / 5
r = hashcode - (a * 5)
s = ''
s += chr((a >> 0) & 0xFF)
s += chr((a >> 8) & 0xFF)
s += chr((a >> 16) & 0xFF)
s += chr((a >> 24) & 0xFF)

s += chr((a >> 0) & 0xFF)
s += chr((a >> 8) & 0xFF)
s += chr((a >> 16) & 0xFF)
s += chr((a >> 24) & 0xFF)

s += chr((a >> 0) & 0xFF)
s += chr((a >> 8) & 0xFF)
s += chr((a >> 16) & 0xFF)
s += chr((a >> 24) & 0xFF)

s += chr((a >> 0) & 0xFF)
s += chr((a >> 8) & 0xFF)
s += chr((a >> 16) & 0xFF)
s += chr((a >> 24) & 0xFF)

s += chr(((a >> 0) & 0xFF) + r)
s += chr((a >> 8) & 0xFF)
s += chr((a >> 16) & 0xFF)
s += chr((a >> 24) & 0xFF)
print(len(s))
subprocess.call(["./col", s])
