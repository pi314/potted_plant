from os.path import expanduser

from .plant1 import Plant1

'''
$ pot init          # lists plant types
$ pot init plant1
$ pot feed
'''

DATA_HOME = expanduser('~/.local/share/potted_plant')

def main():
    p = Plant1(DATA_HOME)


main()
