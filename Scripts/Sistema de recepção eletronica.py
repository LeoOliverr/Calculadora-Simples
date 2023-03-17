# Caso um paciente tenha 65 anos ele deverá entrar na fila de prioridade
# O aplicativo deve ser capaz de perguntar ao cliente se ele possui alguma doença contagiosa, e se sim encaminha-lo para uma sala reservada
# Caso um paciente tenha menos de 18 anos ele deverá ser acompanhado por seu responsável, precisar ir para sala reservada seu responsável o acompanha

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
doenca_contagiosa = input('Você possui alguma suspeita de doença infecto-contagiosa?').upper()
while doenca_contagiosa != 'SIM' and doenca_contagiosa != 'NAO':
        print('Responda com SIM ou NAO!')
        doenca_contagiosa = input('Você possui alguma suspeita de doença infecto-contagiosa?').upper()
if idade >= 65 and doenca_contagiosa == 'SIM':
    print('O paciente {} deve ser inserido em uma fila de prioridade\nEle deve ser encaminhado para a sala reservada'.format(nome))
elif idade < 65 and idade >= 18 and doenca_contagiosa == 'SIM':
    print('O paciente {} não deve ser inserido em uma fila de prioridade\nEle deve ser encaminhado para a sala reservada'.format(nome))
elif idade >= 65 and doenca_contagiosa == 'NAO':
    print('O paciente {} deve ser inserido em uma fila de prioridade\nE pode permanecer na sala comum'.format(nome))
elif idade < 65 and idade >=18 and doenca_contagiosa == 'NAO':
    print('O paciente {} não deverá ser inserido em uma fila de prioridade\nE pode permanecer na sala comum'.format(nome))
elif idade < 18 and doenca_contagiosa == 'SIM':
    print('O paciente {} não deverá ser inserido em uma fila de prioridade\nEle deve ser encaminhado para a sala reservada junto de seu responsável'.format(nome))
else:
    print('O paciente {} não deverá ser inserido em uma fila de prioridade\nE pode permanecer na sala comum junto de seu responsável'.format(nome))
    