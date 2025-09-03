from pwn import xor
puzzle_hex = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
puzzle_bytes = bytes.fromhex(puzzle_hex)
for i in range(128) :
    ans = xor(puzzle_bytes, i)
    if b'crypto' in ans:
        print(i)
        print(ans.decode())

res = xor(puzzle_bytes, b'secret')
print(res.decode('utf-8'))
