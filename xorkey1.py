from pwn import xor
puzzle_hex = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
puzzle_bytes = bytes.fromhex(puzzle_hex)
secret = xor(puzzle_bytes, b'crypto{') # hint from challenge
print(secret.decode('utf-8'))
res = xor(puzzle_bytes, b'myXORkey')
print(res.decode('utf-8'))
