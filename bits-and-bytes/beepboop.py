import sys
import tty
import termios

attrs = termios.tcgetattr(0)
tty.setcbreak(0)

def run():
    while True:
        try:
            val = sys.stdin.read(1)
            for _ in range(int(val)):
                sys.stdout.buffer.write(b'\x07')
            sys.stdout.buffer.flush()
        except ValueError:
            print("That's not an number!")
            

try: 
    run()
finally:
    termios.tcsetattr(0, termios.TCSADRAIN, attrs)
