menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>'''

saldo = 0
limite = 500
extrato = ''
num_saques = 0
LIM_SAQUES = 5

while True:
    opcao = input(menu)

    if opcao == 'd':
        valor = float(input('Informe o valor para depósito: '))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
        else:
            print('Operação falhou! Valor informado é iválido.')

    elif opcao == 's':
        valor = float(input('Informe o valor do saque: '))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = num_saques >= LIM_SAQUES

        if excedeu_saldo:
            print('Operaçao falhou! Você não tem saldo suficiente.')
        elif excedeu_limite:
            print('Operação falhou! O valo do saque excede o limite.')
        elif excedeu_saques:
            print('Operação falhou! Número máximo de saques ecedido.')
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            num_saques += 1
        else:
            print('Operação falhou! O valor informado é inválido.')

    elif opcao == 'e':
        print('\n=============== EXTRATO ===============')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('========================================')

    elif opcao == 'q':
        break

    else:
        print('Operação inválida. Por favor, selecione novamente a operação desejada.')

