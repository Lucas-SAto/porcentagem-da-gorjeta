valor_da_conta = float(input('digite o valor da conta: '))
gorjeta = float(input('digite a porcentagem da gorjeta: '))
porcentagem_da_gorjeta = (gorjeta / 100) * valor_da_conta 
valor_da_gorjeta = print(f'valor da gorjeta: {porcentagem_da_gorjeta}')
total = porcentagem_da_gorjeta + valor_da_conta
conta_final = print(f'total a pagar:{total}')

