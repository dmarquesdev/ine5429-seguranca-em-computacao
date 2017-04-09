'''
Algoritmo Xorshift
Baseado em: https://en.wikipedia.org/wiki/Xorshift
'''
import random

# Inicializa a variavel responsavel por armazenar
# a 'seed', sendo que caso nenhum valor tenha sido
# informado, escolhe um valor aleatorio de 'length' bits
def init_seed(length, seed=None):
    global x
    x = random.getrandbits(length) if seed == None else seed

# Implementacao do Xorshift
def xorshift(length):
    # Efetua o xor (^=) e o shift (<< e >>)
    # baseado nos valores disponiveis na fonte
    # citada
    global x
    x ^= (x << 13)
    x ^= (x >> 7)
    x ^= (x << 5)

    # Aplica uma mascara para limitar o resultado a
    # no maximo 'length' bits
    return x & ((1 << length) -1)

# Funcao chamada ao iniciar o script
def main():
    print '[*] Xorshift Pseudo Random Number Generator'
    # Valores que devem ser testados
    values = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
    # Itera sobre os valores
    for val in values:
        # Chama o inicializador de seed
        init_seed(val)
        print '\n[*] %d bits:' % val
        for i in xrange(10):
            # Armazena em x o resultado do algoritmo de Xorshift
            x = xorshift(val)
            # Imprime o resultado
            print '\t%d) %d' % (i+1, x)

if __name__ == '__main__':
    main()
