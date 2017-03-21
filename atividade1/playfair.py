#!/usr/bin/python2

KEY = 'INFOSEC'
PLAINTEXT = 'DIEGO'
# J is omitted, assuming I=J
FULL_ALPHABET = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'

def getPlayFairTable(key):
    # Remove duplicate characters from key
    key_chars = list(set(key))

    remains = [c for c in FULL_ALPHABET if c not in key]
    alphabet = list(key) + remains

    # Remove J from alphabet
    alphabet = [c for c in alphabet if c != 'J']

    table = ['' for i in xrange(5)]
    table[0] = alphabet[0:5]
    table[1] = alphabet[5:10]
    table[2] = alphabet[10:15]
    table[3] = alphabet[15:20]
    table[4] = alphabet[20:25]

    return table

def getDigraphs(text):
    i = 0
    digs = []
    while i < len(text) - 1:
        dig = text[i:i+2]
        # Add an 'X' to repeated characters
        if dig[0] == dig[1]:
            dig = [dig[0], 'X']
        digs.append(list(dig))
        i += 2

    # Even number padding
    if len(text) % 2 != 0:
        digs.append([text[-1], 'X'])

    return digs

def getLocation(table, char):
    # Make J = I
    if char == 'J':
        return getLocation(table, 'I')

    for i in xrange(len(table)):
        for j in xrange(len(table[i])):
            if table[i][j] == char:
                return (i, j)

def encryptDigraphs(table, digraphs):
    result = ''
    for dig in digraphs:
        row1, col1 = getLocation(table, dig[0])
        row2, col2 = getLocation(table, dig[1])
        if row1 == row2:
            result += table[row1][col1 + 1] + table[row2][col2 + 1]
        elif col1 == col2:
            result += table[row1 + 1][col1] + table[row2 + 1][col2]
        else:
            result += table[row1][col2] + table[row2][col1]

    return result


def cipher(text, key):
    table = getPlayFairTable(key)
    digraphs = getDigraphs(text)
    ciphered_text = encryptDigraphs(table, digraphs)
    return ciphered_text

def main():
    print 'PlayFair Cipher'
    print 'Plain Text: %s' % PLAINTEXT
    print 'Key: %s' % KEY
    print 'Ciphered Text: %s' % cipher(PLAINTEXT.upper(), KEY.upper())

if __name__ == '__main__':
    main()
