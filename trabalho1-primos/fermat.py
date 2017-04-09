"""
Algoritmo de Teste de Primalidade de Fermat
Baseado em: https://en.wikipedia.org/wiki/Fermat_primality_test
"""

import random

def is_prime(n, k):
    # Elimina os casos obvios
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False

    for _ in xrange(k):
        # Escolhe aleatoriamente um numero inteiro
        # entre 2 e n (1 < a < n)
        a = random.randrange(2, n)
        # Calcula a^n-1 mod n
        x = pow(a, n-1, n)
        # Caso x = 1, continue testando
        if x == 1:
            continue
        # Caso contrario, o numero eh composto
        # e a eh uma testemunha de Fermat de que
        # n era composto
        else:
            return False
    # n POSSIVELMENTE eh primo
    return True

def main():
    print '[*] Fermat'
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
            # Armazena em x o resultado do algoritmo de Fermat
            prime = is_prime(rand, 40)
            # Imprime o resultado
            if prime:
                print '\t%d) %d' % (i+1, rand)
                i += 1

if __name__ == '__main__':
    main()

