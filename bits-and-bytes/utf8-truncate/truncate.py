


if __name__ == "__main__":
    print("hi")
    with open('cases', 'rb') as f, open("out", 'wb') as o:
        while True:
            utf = f.readline()
            if len(utf) == 0:
                break
            
            # print(utf[0], len(utf[1:]))
            length = utf[0]
            # print(type(utf[0]))
            o.write(utf[1:length])
            o.write(str.encode('\n'))
            print(utf[0:length])
