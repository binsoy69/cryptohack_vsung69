import base64
hex = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
base64_decode = bytes.fromhex(hex)
base64_encode = base64.b64encode(base64_decode)
print(base64_encode.decode())
