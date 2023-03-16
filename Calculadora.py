reutilizar = True

def somar(valor1, valor2):
    soma = valor1 + valor2
    print('A soma é: {0:.2f}'.format(soma))

def subtrair(valor1, valor2):
    subtracao = valor1 - valor2
    print('A subtração é: {0:.2f}'.format(subtracao))

def dividir(valor1, valor2):
    if(valor2 == 0):
        print("Não é possivel dividir por zero.")
    else:
        divisao = valor1 / valor2
        print('A divisão é: {0:.2f}'.format(divisao))

def multiplicar(valor1, valor2):
    multiplicação = valor1 * valor2
    print('A multiplicação é: {0:.2f}'.format(multiplicação))
while(reutilizar is True):
    valor1 = float(input('Digite o primeiro valor: '))
    valor2 = float(input('Digite o segundo valor: '))
    print('Escolha a operação desejada\nAdição: 1 \nSubtração: 2 \nDivisão: 3 \nMultiplicação: 4')
    decisao = input('Digite qual operação deve ser feita: ')

    if int(decisao) == 1:
        somar(valor1, valor2)
    elif int(decisao) == 2:
        subtrair(valor1, valor2)
    elif int(decisao) == 3:
        dividir(valor1, valor2)
    elif int(decisao) == 4:
        multiplicar(valor1, valor2)
    else:
        print('Opção inválida')
