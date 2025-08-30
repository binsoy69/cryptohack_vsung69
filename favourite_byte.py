from pwn import xor

puzzle_hex = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
puzzle_bytes = bytes.fromhex(puzzle_hex)
for i in range(256):
    ans = xor(puzzle_bytes, i)
    if b"crypto" in ans:
        print(i)
        print(ans.decode())