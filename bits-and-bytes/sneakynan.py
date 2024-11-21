def conceal(input :str) -> float:
    bits = bytes(input, 'utf-8')
    
    length = len(bits)
    out = [0x7f, 0b11111000 | length]
    for i in range(6-length):
        out.append(0x00)
    for b in bits:
        out.append(b)
    return struct.unpack('>d', bytes(out))[0]

def extract(non: float) -> str:
    b = struct.pack('>d', non)
    length = b[1] & 0b00000111
    message = b[8-length:]
    return message.decode("utf-8")

if __name__ == "__main__":
    import struct
    assert extract(conceal("Hello!")) == "Hello!"
    assert extract(conceal("Hello")) == "Hello"
    assert extract(conceal("Hell")) == "Hell"
    assert extract(conceal("Hel")) == "Hel"
    assert extract(conceal("He")) == "He"
    assert extract(conceal("H")) == "H"
    