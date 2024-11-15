import os

if os.path.exists('rotated.bmp'):
    os.remove('rotated.bmp')

with open('teapot.bmp', 'rb') as f, open('rotated.bmp', 'wb') as s:

    
    res = f.read()
    start_address= int.from_bytes(res[10:11], "little")
    height = int.from_bytes(res[18:22], "little")
    width = int.from_bytes(res[22:26], "little")
    out=0
    out <<= start_address
    
    img = res[start_address:]
    out = res[0:start_address]
    out += res[0:start_address]
    print(start_address)
    print(res[18:22], res[22:26])
    print(type(out))
    n=bytearray(res)
    for i, b in enumerate(n):
        if i>= start_address:
            n[i] = 0
    s.write(bytes(n))