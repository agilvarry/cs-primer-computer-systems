if __name__ == "__main__":
    from sys import stdout
    with open('cases', 'rb') as f:
        while True:
            utf = f.readline()
            line = utf[1:-1]
            if len(utf) == 0:
                break 
            out = [] 
            emoji=[]
            for i, b in enumerate(line[:utf[0]]):
                if b & 0x80 == 0:
                    out.append(b)
                if b & 0x80 != 0:
                    emoji.append(b)
                    try:
                        bytes(emoji).decode("utf-8")
                        out = out + emoji
                        emoji=[]
                    except:
                        continue
            stdout.write(bytes(out).decode("utf-8"))
            stdout.write('\n')
