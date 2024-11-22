print('PRIMEIRA RODADA')

# Entrada da primeira rodada
hora1 = int(input('Insira o número da hora de ENTRADA (1 a 24): '))
while hora1 < 1 or hora1 > 24:
    print('Formato Inválido! Insira um número de 1 a 24.\n')
    hora1 = int(input('Insira o número da hora de ENTRADA (1 a 24): '))

minutos1 = int(input('Insira o número dos minutos de ENTRADA (0 a 59): '))
while minutos1 < 0 or minutos1 > 59:
    print('Formato Inválido! Insira um número de 0 a 59.\n')
    minutos1 = int(input('Insira o número dos minutos de ENTRADA (0 a 59): '))

# Saída da primeira rodada
hora1_pausa = int(input('Insira o número da hora de SAÍDA (1 a 24): '))
while hora1_pausa < 1 or hora1_pausa > 24:
    print('Formato Inválido! Insira um número de 1 a 24.\n')
    hora1_pausa = int(input('Insira o número da hora de SAÍDA (1 a 24): '))

minutos1_pausa = int(input('Insira o número dos minutos de SAÍDA (0 a 59): '))
while minutos1_pausa < 0 or minutos1_pausa > 59:
    print('Formato Inválido! Insira um número de 0 a 59.\n')
    minutos1_pausa = int(
        input('Insira o número dos minutos de SAÍDA (0 a 59): '))

#############################################################

print('SEGUNDA RODADA')

# Entrada da segunda rodada
hora2 = int(input('Insira o número da hora de ENTRADA (1 a 24): '))
while hora2 < 1 or hora2 > 24:
    print('Formato Inválido! Insira um número de 1 a 24.')
    hora2 = int(input('Insira o número da hora de ENTRADA (1 a 24): '))

minutos2 = int(input('Insira o número dos minutos de ENTRADA (0 a 59): '))
while minutos2 < 0 or minutos2 > 59:
    print('Formato Inválido! Insira um número de 0 a 59.')
    minutos2 = int(input('Insira o número dos minutos de ENTRADA (0 a 59): '))

# Saída da segunda rodada
hora2_pausa = int(input('Insira o número da hora de SAÍDA (1 a 24): '))
while hora2_pausa < 1 or hora2_pausa > 24:
    print('Formato Inválido! Insira um número de 1 a 24.')
    hora2_pausa = int(input('Insira o número da hora de SAÍDA (1 a 24): '))

minutos2_pausa = int(input('Insira o número dos minutos de SAÍDA (0 a 59): '))
while minutos2_pausa < 0 or minutos2_pausa > 59:
    print('Formato Inválido! Insira um número de 0 a 59.')
    minutos2_pausa = int(
        input('Insira o número dos minutos de SAÍDA (0 a 59): '))

#############################################################

print('TERCEIRA RODADA')

# Entrada da terceira rodada
hora3 = int(input('Insira o número da hora de ENTRADA (1 a 24): '))
while hora3 < 1 or hora3 > 24:
    print('Formato Inválido! Insira um número de 1 a 24.')
    hora3 = int(input('Insira o número da hora de ENTRADA (1 a 24): '))

minutos3 = int(input('Insira o número dos minutos de ENTRADA (0 a 59): '))
while minutos3 < 0 or minutos3 > 59:
    print('Formato Inválido! Insira um número de 0 a 59.')
    minutos3 = int(input('Insira o número dos minutos de ENTRADA (0 a 59): '))

# Saída da terceira rodada
hora3_pausa = int(input('Insira o número da hora de SAÍDA (1 a 24): '))
while hora3_pausa < 1 or hora3_pausa > 24:
    print('Formato Inválido! Insira um número de 1 a 24.')
    hora3_pausa = int(input('Insira o número da hora de SAÍDA (1 a 24): '))

minutos3_pausa = int(input('Insira o número dos minutos de SAÍDA (0 a 59): '))
while minutos3_pausa < 0 or minutos3_pausa > 59:
    print('Formato Inválido! Insira um número de 0 a 59.')
    minutos3_pausa = int(
        input('Insira o número dos minutos de SAÍDA (0 a 59): '))

#############################################################

print('QUANTIA TOTAL DO DIA')

# Total recebido no dia
quantia_total_dia = float(input(
    'Insira o valor total recebido no dia (somente números e utilize ponto ao invés de vírgula): '))
while quantia_total_dia <= 0:
    print('Formato Inválido! Insira um número maior ou igual a zero.')
    quantia_total_dia = float(input(
        'Insira o valor total recebido no dia (somente números e utilize ponto ao invés de vírgula): '))

# Cálculo do total de minutos e valor por hora

soma_rodada1 = ((hora1_pausa * 60) + minutos1_pausa) - \
    ((hora1 * 60) + minutos1)

soma_rodada2 = ((hora2_pausa * 60) + minutos2_pausa) - \
    ((hora2 * 60) + minutos2)

soma_rodada3 = ((hora3_pausa * 60) + minutos3_pausa) - \
    ((hora3 * 60) + minutos3)

soma_total_rodadas = soma_rodada1 + soma_rodada2 + soma_rodada3

valor_hora = (quantia_total_dia / soma_total_rodadas) * 60

print(f'O valor da sua hora foi de: R$ {valor_hora:.2f}')
