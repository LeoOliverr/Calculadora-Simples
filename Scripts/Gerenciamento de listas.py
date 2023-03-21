inventario = []
reutilizar = 'SIM'
adicionar = 'SIM'
buscar = 'SIM'
deletar = 'SIM'

def adicionarInventario(inventario):
    adicionar = (input('Caso queira adicionar algum item a lista digite sim: ')).upper()
    while adicionar == 'SIM':
        equipamentos = [input('Digite o nome do equipamento: '),
                        int(input('Digite o numero serial do equipamento: ')),
                        float(input('Digite o valor do equipamento: '))]
        inventario.append(equipamentos)
        adicionar = input('Digite Sim Se quiser adicionar mais itens').upper()

def deletarInventario(inventario):
    deletar = input('Caso queira deletar algum item da lista digite sim: ').upper()
    while deletar == 'SIM':
        deletar_ser = int(input('Digite o numero serial do item a ser deletado: '))
        for indice in inventario:
            if indice[1] == deletar_ser:
                inventario.remove(indice)
                print('O item foi deletado com sucesso!')
        deletar = input('Digite sim se deseja continuar deletando itens da lista: ')

def buscarInventario(inventario):
    buscar = input('Caso queira buscar algum item dessa lista digite sim: ').upper()
    while buscar == 'SIM':
        busca = input('Digite o nome do equipamento que deseja buscar na lista: ')
        for indice in inventario:
            if busca == indice[0]:
                print('Nome: ', indice[0])
                print('Serial: ', indice[1])
                print('Valor: ', indice[2])
        buscar = input('Digite sim se deseja continuar buscando por itens da lista: ').upper()

def analiseValores(inventario):
    valores = []
    for indice in inventario:
        valores.append(indice[2])
    if len(valores) > 0:
        print('O equipamento de maior valor custa: ', max(valores))
        print('O equipamento de menor valor custa: ', min(valores))
        print('A soma dos valores dos equipamentos é: ', sum(valores))

while reutilizar == 'SIM':
    adicionarInventario(inventario)
    deletarInventario(inventario)
    buscarInventario(inventario)
    analiseValores(inventario)


    reutilizar = input('Digite sim para continuar utilizando o programa: ').upper()
