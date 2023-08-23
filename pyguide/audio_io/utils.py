import sys
import select
import msvcrt

def key_pressed():
    # windows
    if sys.platform == "win32":
        return msvcrt.kbhit()
    # UNIX-like systems
    else:  
        i, o, e = select.select([sys.stdin], [], [], 0.1)
        return (i != [])