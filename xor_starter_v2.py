from pwn import *
res = xor("label".encode(), 13)
print(res.decode())