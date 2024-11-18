import os

if os.path.exists('rotated.bmp'):
    os.remove('rotated.bmp')

with open('stretch-goal.bmp', 'rb') as file, open('stretch-rotated.bmp', 'wb') as s:
    f = file.read()
    
    start_address= int.from_bytes(f[10:11], "little")
    # height = int.from_bytes(f[18:22], "little")
    width = int.from_bytes(f[22:26], "little")
    s.write(f[:start_address])

    img = f[start_address:]
    
    new_rows = [ [] for _ in range(width)]
    pixels = [img[i: i+3] for i in range(0, len(img), 3)]
    rows = [pixels[i: i+width] for i in range(0, len(pixels), width)]
    
    for row in rows:
        for j, pixel in enumerate(row):
            new_rows[j].append(pixel)

    for row in reversed(new_rows):
       for pixel in row:
            s.write(bytes(pixel))
