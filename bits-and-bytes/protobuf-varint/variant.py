"""
-read the files with hexdump?
-interpret as int

implement variant encoder

implement decoder

  # out =[]
  # n = int.from_bytes(n, 'big')
  # while n > 0:

  #   part = n & 0x7F
  #   out.append(part)

  #   n>>=8
  # print(bytes(out))
  # r = functools.reduce(lambda a, b: a+b, list(bytes(out)))
  # print(r)

  # def encode(n):
#   out=[]
#   while n > 0: #todo, checking for 0 twice
#     part = n & 0x7F #bitmask???

#     n>>=7
#     if n>0:
#       part |= 0x80

#     out.append(part)
#   return bytes(out)

"""
def ndecode(n):
  accum = 0
  for i in reversed(n):
    accum <<= 7
    accum += (i & 0x7F)
  return accum

def decode(n):
  b = ''.join(format(byte, '08b') for byte in n)
  out = ""
  while len(b) > 0:
    part = b[1:8] 
    b = b[8:]
    out= part + out
  return int(out, 2)

def encode(n):
  def encode(n, accum):
    part = n & 0x7F
    n >>= 7
    if n>0:
      part |= 0x80
      accum.append(part)
      return encode(n, accum)
    accum.append(part)
    return bytes(accum)
  return encode(n, [])

if __name__ == "__main__":
  import struct
  cases =(
    ('1.uint64', b'\x01'),
    ('150.uint64', b'\x96\x01'),
    ('maxint.uint64', b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01')
  )
  for file, encode_res in cases:
    with open(file, 'rb') as f:
      n = struct.unpack('>Q', f.read())[0]
      assert encode(n) == encode_res
      assert decode(encode_res) == n
      assert ndecode(encode_res) == n

