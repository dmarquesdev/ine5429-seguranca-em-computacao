#!/usr/bin/python2

from itertools import cycle

KEY = 'INFOSEC'
PLAINTEXT = 'DIEGO'

def cipher(text, key):
    result = ''
    # Zip gets two lists and iterates through it combining all elements with
    # the same index on the other list.
    #
    # Cycle iterates through a list going back to the start
    # when the end is reached, just like is needed on Vigenere Algorithm.
    for comb in zip(text, cycle(key)):
        if ord(comb[0]) >= ord('A') and ord(comb[0]) <= ord('Z'):
            result += chr(ord('A') + ((ord(comb[0]) + ord(comb[1])) % 26))

    return result

def main():
    print 'Vigenere Cipher'
    print 'Plain Text: %s' % PLAINTEXT
    print 'Key: %s' % KEY
    print 'Ciphered Text: %s' % cipher(PLAINTEXT.upper(), KEY.upper())

if __name__ == '__main__':
    main()
