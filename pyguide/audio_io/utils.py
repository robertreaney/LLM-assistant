import sys

def key_pressed():
    # windows
    if sys.platform == "win32":
        import msvcrt
        return msvcrt.kbhit()
    # UNIX-like systems
    else:  
        import select
        i, o, e = select.select([sys.stdin], [], [], 0.1)
        return (i != [])