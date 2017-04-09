"""
Algoritmo Teste de Primalidade de Miller-Rabin
Baseado em: https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
"""

import random

def is_prime(n, k):
    # Elimina os casos obvios
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False

    # Escreve n-1 como 2^r * d
    # com 'd' impar atraves da fatoracao de
    # potencias de 2 de n-1
    r = 0
    d = n-1

    while d % 2 == 0:
        r += 1
        d //= 2

    # Itera por k (numero de 'precisao'), procurando por
    # numeros que "testemunhem" que n eh primo
    for i in xrange(0, k):
        # Escolhe um inteiro aleatorio nos limites [2, n-2]
        a = random.randrange(2, n-1)

        # Efetua a^d mod n
        x = pow(a, d, n)
        if x == 1 or x == n-1:
            continue

        for j in xrange(0, r-1):
            # Efetua x^2 mod n
            x = pow(x, 2, n)
            # Caso x = 1, n eh composto
            if x == 1:
                return False
            # Caso contrario, mais um numero de testemunha
            # precisa ser considerado
            if x == n - 1:
                break
        # n eh composto
        return False
    # n POSSIVELMENTE eh primo
    return True

def main():
    print '[*] Miller-Rabin'
    # Valores que devem ser testados
    values = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
    # Itera sobre os valores
    for val in values:
        print '\n[*] %d bits:' % val
        i = 0
        while i < 10:
            # Gera um numero pseudoaleatorio de 
            # 'val' bits
            rand = random.getrandbits(val)
            # Armazena em x o resultado do algoritmo de Miller-Rabin
            prime = is_prime(rand, 40)
            # Imprime o resultado (somente se for primo)
            if prime:
                print '\t%d) %d' % (i+1, rand)
                i += 1

if __name__ == '__main__':
    main()
