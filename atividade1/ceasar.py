#!/usr/bin/python2

ALPHABET_LIMIT = 90
PLAINTEXT = 'DIEGO'
ROTATION = 3

def cipher(text, rotation):
    cipher_text = ''
    for char in text:
        ciphered = chr(ord(char) + rotation - 26) if (ord(char.upper()) + rotation) > ALPHABET_LIMIT else chr(ord(char) + rotation)
        cipher_text += ciphered

    return cipher_text

def main():
    print 'Ceasar Cipher'
    print 'Plain Text: %s' % PLAINTEXT
    print 'Rotation: %d' % ROTATION
    print 'Ciphered Text: %s' % cipher(PLAINTEXT, ROTATION)

if __name__ == '__main__':
    main()
