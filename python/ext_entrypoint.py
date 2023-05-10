from argparse import ArgumentParser
from main import main

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-i', '--input', type=str)

    args = parser.parse_args()

    temp = main((args.input,))
    append_comments = ['# ' + x + '\n' for x in temp.split('\n')]


    print(f"""
###########################
# Generated Code from LLM-A
#
{''.join(append_comments)}
#
# End (LLM-A)
############################
""")    