# calculadora em python 

while true
    print ('Calculadora do mal em cobra')
    import os

    #Variáveis 
    numero_1 = str(input('Informe um número: ')).replace(',' , '.')
    numero_2 = str(input('Informe um número: ')).replace(',' , '.')

    # conversão das varáveis  
    numero_1 - float(numero_1)
    numero_2 - float(numero_2)

    # limpa tela
    os.system('cls')

    # operações matemátca

    print ('Informe a operação matemática que deseja fazer\n')
    print ('Para somar digite "+"')
    print ('Para subrtrair digite "-"')
    print ('Para multiplicar digite "*"')
    print ('Para dividir digite "/"')
    print ('Para encontrar o resto digite "%"')

    op = input('Informe qual a operação desejada')

    match op:
        case '+': 
            print (f'A soma é {numero_1 + numero_2}.')
        case '-':
            print (f'A subtração é {numero_1 - numero_2}.')
        case '*':
            print (f'A multiplicação é {numero_1 * numero_2}.')
        case '/':
            print (f'A divisão é {numero_1 / numero_2}.')
        case '%':
            print (f'O resto da divisão é {numero_1 % numero_2}.')
            continue
    


