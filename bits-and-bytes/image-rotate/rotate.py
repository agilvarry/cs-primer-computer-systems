import os

if os.path.exists('rotated.bmp'):
    os.remove('rotated.bmp')

with open('teapot.bmp', 'rb') as file, open('rotated.bmp', 'wb') as s:
    f = file.read()
    start_address= int.from_bytes(f[10:11], "little")
    height = int.from_bytes(f[18:22], "little")
    width = int.from_bytes(f[22:26], "little")
    out=[]
    img = f[start_address:]
    img_len = len(img)
    s.write(f[:start_address])
    quarter_len = img_len//4
    quarter_one = f[start_address: quarter_len]
    rest = f[quarter_len:]
    
    out = bytearray()
    
    # out <<= quarter_len
    # out.append(rest)
    # out.append(quarter_one)
    # b = bytes(out) 
    s.write(bytes(b for b in rest))
    s.write(bytes(b for b in quarter_one))
    # im
    # print(img_len)
    # for i, b in enumerate(n):
    #     if i>= start_address:
    #         n[i] = 0
    # s.write(bytes(n))