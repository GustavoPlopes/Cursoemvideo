def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            ok = True
            valor = int(n)
        else:
            print('\033[0;31m!ERRO! Digite um número valido.\033[m')
        if ok:
            break
    return valor
    
n = leiaint('Digite um número: ')
print(f'Você digitou o número {n}')