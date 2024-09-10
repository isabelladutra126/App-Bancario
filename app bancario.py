menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

"""
extrato = []
qtd_saque = 0
valor_deposito = 0
valor_saque = 0
saldo = 0

while True:

    opcao = input(menu)

    if opcao == "1":
        valor_deposito = float(input("Digite o valor em R$ a ser depositado: R$ "))
        extrato.append(f"Depósito de +{valor_deposito}")
        saldo += valor_deposito
        print("Valor depositado com sucesso.")
        if valor_deposito < 0:
            print("Por favor, digite um valor positivo.")


    elif opcao == "2":
        if valor_deposito > 0:
            valor_saque = float(input("Digite em reais o valor que deseja sacar: R$ "))
            if qtd_saque > 3 or valor_saque > 500:
                print("Limite diário de saque atingido! (não é permitido mais de 3 saques por dia ou saque "
                      "maior que 500 reais.)")
            else:
                qtd_saque += 1
                saldo -= valor_saque
                extrato.append(f" Saque de R${valor_saque}")
                print(f"Você sacou R${valor_saque}.")


    elif opcao == "3":
        if len(extrato) == 0:
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
            print(f"Seu saldo final é de R${saldo}.")

    if opcao == "4":
        print("Obrigado por usar nosso sistema. Encerrando...")
        break