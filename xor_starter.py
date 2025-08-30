# without using pwntools

ascii_char = "label"
ascii_val = [ord(c) for c in ascii_char]
print(ascii_val)
dec_to_bin = [bin(x)[2:].zfill(8) for x in ascii_val]
print(dec_to_bin)
num_to_xor = bin(13)[2:].zfill(8)
print(num_to_xor)
xor_res = [int(b, 2) ^ int(num_to_xor, 2) for b in dec_to_bin]
print(xor_res)
ascii_res = [chr(x) for x in xor_res]
print(ascii_res)
