import datetime

#  DECLARAÇÃO DAS INFORMAÇÕES DOS DISCOS
nome = ['amor', 'batida', 'sentadinha', 'familia']
artista = ['madona', 'alok', 'annita', 'timaia']
anoLanc = ['2001', '2018', '2016', '2000']
estilo = ['pop', 'eletronica', 'funk', 'classico']
quantidade = ['30', '40', '50', '20']
indices = range(0, len(nome))

# CRIANDO UMA FUNÇÃO PARA LER OS DISCOS DISPONÍVEIS
def listar_discos(nome, artista, anoLanc, estilo, quantidade):
    print('#########DISCOS DISPONIVEIS#########')
    for indice in indices:
        print('[' + str(indice) + ']', nome[indice], '|' + str(artista[indice]), '|' + str(anoLanc[indice]),
              '|' + str(estilo[indice]), '|' + str(quantidade[indice]) + '|')


listar_discos(nome, artista, anoLanc, estilo, quantidade)


pedidos = []
total = 0

# CRIANDO A PRIMEIRA FUNÇÃO PARA FAZER PEDIDO DE DISCOS CONTIDO NA LISTA
def fazer_pedido() -> int:
    pedido = int(input('Qual produto? '))
    return pedido


print('###### PEDIDO: ######')


while True:
    for pedido in range(1):
     pedido = fazer_pedido()
     pedidos.append(pedido)



      # CRIANDO UMA FUNÇÃO PARA IMPRIMIR PEDIDO REALIZADO
    def imprimir_recibo(pedidos: list, total: int, nome: int, artista: int, anoLanc: int, estilo: int):
            print('###### RECIBO: ######')
            pedido = fazer_pedido()
            pedidos.append(pedido)

            for pedido in pedidos:
                print('[' + str(pedido) + ']' + str(nome[pedido]),
                      '|' + str(artista[pedido]) + '|', + str(anoLanc[pedido]), '|' + str(estilo[pedido]) + '|')
    print('##PEDIDO CONCLUÍDO##')
    print('###### TOTAL: ######')
    print((pedidos, nome[pedido], artista[pedido], anoLanc[pedido], estilo[pedido]))

    break

    # PARA ADICIONAR A REGRA QUE FOI PEDIDA NA DOCUMENTAÇÃO DO DESAFIO , FIZ UMA SIMULAÇÃO DE OUTRA FUNÇÃO
    # FAZENDO COM QUE O USUARIO SIMULASSE A HORA VINDO DE UMA VARIÁVEL DEFINIDA POR MEIA NOITE (0)

pedidos2 = []
total2 = 1
""" 
   1 - Criar uma comparação da hora atual com meia noite;
   2 - Fazer com que o usuario consiga simular que a hora atual é meia noite

"""
#OPERAÇÃO PARA TESTE DE HORA ATUAL SENDO MEIA NOITE




def fazer_pedido_limitado(horaAtual, pedidolimitado = None) -> int: # PEDIDO LIMITADO DOS 500 DISCOS QUE SERÃO LANÇADOS


    if pedidolimitado == 'S' and horaAtual >= 0:

        #LANÇAMENTO DOS NOVOS DISCOS AS 00:00
        nome = ['We are Reactive']
        artista = ['Hohpe']
        anoLanc = ['2022']
        estilo = ['Romântico']
        quantidade = ['500']
        indices = range(0, len(nome))

        # LISTANDO DISCOS DISPONIVEIS DEPOIS DA MEIA NOITE
        def listar_discos_limitados(nome, artista, anoLanc, estilo, quantidade):
            print('#########DISCOS DISPONIVEIS#########')
            for indice in indices:
                print('[' + str(indice) + ']', nome[indice], '|' + str(artista[indice]), '|' + str(anoLanc[indice]),
                      '|' + str(estilo[indice]), '|' + str(quantidade[indice]) + '|')

        listar_discos_limitados(nome, artista, anoLanc, estilo, quantidade)

        pedido2 = int(input('Qual produto? '))
    elif pedidolimitado == 'N':
          print('Pedido finalizado')
          return



# SIMULANDO A HORA ATUAL COM A ATRIBUIÇÃO DA VARIAVEL , RANGE(500) PARA 500 PEDIDOS
while True:
    for pedido2 in range(5):
        horaAtual = datetime.datetime.now().hour
        simulaHora = (input('Deseja simular a hora atual? (S|N)'))
        if simulaHora == 'S':
            pedidolimitado = (input('Deseja fazer um pedido do novo disco limitado? (S|N) '))
            pedido2 = fazer_pedido_limitado(horaAtual, pedidolimitado)
            pedidos2.append(pedido2)
            horaAtual = 0

        else:
            pedido2 = fazer_pedido_limitado(horaAtual)
            pedidos2.append(pedido2)







        def imprimir_recibo2(pedidos: list, total: int, nome: int, artista: int, anoLanc: int, estilo: int):
             print('###### RECIBO: ######')
             pedido = fazer_pedido_limitado()
             pedidos.append(pedido)
             total += indices[pedido]  # incremento
             for pedido in pedidos:
                 print('[' + str(pedido) + ']' + str(nome[pedido]),
                       '|' + str(artista[pedido]) + '|', + str(anoLanc[pedido]), '|' + str(estilo[pedido]) + '|')


             print('##PEDIDO CONCLUÍDO##')
             print('###### TOTAL: ######')
             print((pedidos, nome[pedido], artista[pedido], anoLanc[pedido], estilo[pedido]))
    print('Não temos mais esse disco em estoque!')
    break
