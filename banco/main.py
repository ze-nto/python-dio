
total = 0
menu = 1
extrato = "-------Seu Extrato-----------\n\n"

while menu > 0:
  print('''
*******************************************************
    Escolha uma operação:
        1) Depósito
        2) Saque
        3) Extrato
    
    Digite o número da operação ou 0 para sair.
******************************************************\n
  ''')
  menu = int(input("Digite o numero: "))
  if menu == 1: 
    deposito = int(input('Quanto deseja depositar: '))
    extrato += f"-- Depósito: {deposito} reais\n"
    total += deposito
    print(f'Você depositou {deposito}. O total agora é {total}.')
  elif menu == 2:
    saque = int(input('Quanto deseja sacar: '))
    extrato += f"-- Saque: {saque} reais\n"
    total -= saque
    print(f'Você sacou {saque}. O total agora é {total}.')
  elif menu == 3:
    extrato += f'______________________\n Total: {total} \n --------------------------------------------'
    print(f'{extrato}')
  else:
    print('Numero inválido')
