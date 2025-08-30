from pwn import *
res = xor("label", 13)
print(res)