# -*- coding: utf-8 -*-

'''
Realiza apuração dos números sorteados no NatalCap.

O resultado pode ser apurado digitando dezena a dezena,
ou digitando todas as dezenas de uma unica vez.

------------------------------
Instruções de Preenchimento:
------------------------------

Preencha a variável 'sorteio_atual' para informar ao programa que
sorteio está em andamento no momento.

Preencha as variáveis 'cartelas' e 'meus_numeros' com os números
do seu certificado NatalCap.

Preencha as variáveis 'sorteios' e 'numeros_sorte' com as dezenas
sorteadas no NatalCap.

Ao exeuctar o programa será aberto um prompt para digitação
das dezenas sorteadas. Digite um número e tecle enter. Uma nova
dezena será solicitada.

Para parar o programa digite 'sair'. O programa irá imprimir
os resultados.

Ao encerrar o programa o resultado final será impresso. Você poderá
copiar os números sorteados e colar na variável 'sorteios' para realizar
uma apuração total no final.

'''

cartelas = []
sorteios = {}
sorteio_atual = 3

# meus numeros
cartelas.append([
                 [8,9,10,12,14,16,17,21,26,27,32,33,39,41,42,46,50,51,52,57],
                 [1,2,4,9,11,16,18,21,24,28,35,37,40,42,45,48,51,54,56,57],
                ])

meus_numeros_sorte = [139237, 389237]

# Resultados
sorteios.update({1: [],
                 2: [59, 51, 10, 57, 41, 6, 20, 22, 27, 12, 24, 53, 7, 50, 33, 49, 32, 26, 56, 18, 28, 60, 43, 19, 3, 25, 14, 34, 11, 30, 46, 29, 47, 9, 13, 8],
                 3: [47, 36, 34, 24, 19, 48, 49, 59, 46, 41, 16, 55, 3, 17, 5, 15, 56, 23, 27, 38, 57, 7, 9, 25, 10, 6, 45, 31, 51, 11, 12, 43, 50, 58],
                 4: []})

numeros_sorte = []

def print_result():
    result = '''
--------------------------------------------------------
|        Bloco 1         |    |        Bloco 2         | 
--------------------------    --------------------------
| {C101} | {C102} | {C103} | {C104} | {C105} |    | {C201} | {C202} | {C203} | {C204} | {C205} |
--------------------------    --------------------------
| {C106} | {C107} | {C108} | {C109} | {C110} |    | {C206} | {C207} | {C208} | {C209} | {C210} |
--------------------------    --------------------------
| {C111} | {C112} | {C113} | {C114} | {C115} |    | {C211} | {C212} | {C213} | {C214} | {C215} |
--------------------------    --------------------------
| {C116} | {C117} | {C118} | {C119} | {C120} |    | {C216} | {C217} | {C218} | {C219} | {C220} |
--------------------------------------------------------
'''
    global cartelas
    d = {}
    for cartela in range(len(cartelas)):
        print '--------------------------------------------------------'
        print '|               Cartela {cartela} - Sorteio {sorteio_atual}                  |'\
                .format(cartela=cartela +1, sorteio_atual=sorteio_atual)
        for bloco in range(2):
            for dezena in range(20):
                key = ('C' + str(bloco + 1) + ('00'+ str(dezena + 1))[-2:])
                value = ('00'+ str(cartelas[cartela][bloco][dezena]))[-2:]

                value = '  ' if int(value) in sorteios[sorteio_atual] else value
                
                d.update({key: value})
    print result.strip().format(**d)

def get_number():
    result = raw_input('Digite o número Sorteado: ')
    if result == 'sair':
        return
    try:
        result = int(result)
        sorteios[sorteio_atual].append(result)
        print_result()
        get_number()
    except Exception as e:
        print 'Erro: ', e
        print 'Entrada inválida! Tente Novamente ou digite "sair" para cancelar!'
        get_number()

# inicia captura dos numeros
get_number()

# imprime resultado geral
for sorteio in range(1, 5):
    sorteio_atual = sorteio
    print_result()
    print 'Numeros Sorteados: {}'.format(sorteios[sorteio])

print '-------------------------------'
print 'Numeros da Sorte:'
for numero in numeros_sorte:
    print '{}: {} {}'\
        .format(i,
                numero,
                '<-- {} - VOCE GANHOU' if numero in meus_numeros_sorte else ''
                )
    i += 1
print '-------------------------------'
