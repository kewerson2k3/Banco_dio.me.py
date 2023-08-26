menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print ("Operação falhou!. Informe um valor válido.")
    
    elif opcao == "s":
        valor = float(input("Informe o valor de saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo: 
            print ("Operação invalida! Você não tem saldo suficiente na conta.")

        elif excedeu_limite:
            print ("Operação invalida! Valor superior ao permitido")

        elif excedeu_saques:
            print ("Operação invalida! Você atingiu o limite de saques diários")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print ("Operação falhou! O valor informado não é valido.")

    elif opcao == "e":
        print ("\n ===================== EXTRATO =====================")
        print ("Não foram realizadas movimentações em sua conta." if not extrato else extrato)
        print (f'\nSaldo: R$ {saldo:.2f}')
        print ("=====================================================")

    elif opcao == "q":
        (print ("Obrigado por utilizar nossos serviços!"))
        break

    else: 
        print ("Operação invalida, informe novamente a operação desejada.")