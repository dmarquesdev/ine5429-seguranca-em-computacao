'''
Algoritmo Blum Blum Shub PRNG
Baseado em: https://pt.wikipedia.org/wiki/Blum_Blum_Shub
'''

import random
from millerRabin import is_prime

# Lista atulizada para armazenar os 2 valores primos
# utilizados no algoritmo
primes = []

# Inicializa o seed com um numero aleatorio de 32 bits
# (a escolha de 32 bits foi aleatoria, poderia ser 
# qualquer valor) ou com um numero informado a funcao
def init_seed(seed=None, p=None, q=None):
    global x, primes
    x = random.getrandbits(32) if seed == None else seed
    # Caso os primos ainda nao tenham sido achados,
    # calcular os mesmos
    if p == None or q == None or p == q:
        get_primes()
    else:
        primes = []
        primes.append(p)
        primes.append(q)

# Procura por um numero primo n 'bom' que 
# satisfaca a condicao de n mod 4 == 3
# necessaria ao algoritmo
#
# Para encontrar o numero utiliza o 
# metodo de Miller-Rabin com precisao de 10
# bases aleatorias
#
# O tamanho 4096 foi escolhido por ser o 
# maior tamanho do teste, porem apenas
# metade dele eh necessaria
def get_good_prime(length=4096):
    while True:
        n = random.getrandbits(length/2)
        if is_prime(n, k=10) and n % 4 == 3:
            return n

# Preenche a lista dos primos (p e q)
def get_primes():
    global primes
    while len(primes) < 2:
        primes.append(get_good_prime())

def bbs(length):
    global primes
    # Separa os valores p e q utilizados
    # para calcular o modulo
    p, q = primes

    # Calcula a formula do algoritmo
    # Xn+1 = Xn^2 mod M, M = pq
    global x
    for _ in xrange(length):
        x = x**2 % (p*q)

    # Retorna o valor de X passando uma mascara
    # de bits para restringir o valor a 'length'
    # bits
    return x & ((1 << length) - 1)

# Funcao chamada ao iniciar o script
def main():
    print '[*] Blum Blum Shub Pseudo Random Number Generator'
    # Valores que devem ser testados
    values = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
    # Itera sobre os valores
    for val in values:
        # Chama o inicializador de seed
        init_seed()
        print '\n[*] %d bits:' % val
        for i in xrange(10):
            # Armazena em x o resultado do algoritmo
            x = bbs(val)
            # Imprime o resultado
            print '\t%d) %d' % (i+1, x)

if __name__ == '__main__':
    main()
