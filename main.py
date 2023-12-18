menu = """

 [d] Depositar 
 [s] Sacar
 [e] Extrato
 [q] Sair   


==> """

saldo=0
limite=500
extrato=""
numero_saques=0
limite_saques=3
total_deposito=0
total_saque=0

while True:

    opcao = input(menu)

    if opcao == "d":
        print("DEPOSITOS")
        deposito = float( input("Insira a quantidade desejada de deposito:"))
        
        if deposito <=0:
            print("Quantidade depositada esta incorreta")
        else: 
            saldo += deposito
        print(f"Valor de R${deposito: .2f} depositado")
        print(f"Saldo atual de: R${saldo: .2f}")
        extrato = f"Deposito de: R${deposito: .2f}"

    elif opcao == "s":
        print("SAQUES")
        if saldo <= 0 or numero_saques == limite_saques:
           print("Operação não permitida")
        else:
            saque = float(input("Qual valor você deseja sacar?"))
            if saque < saldo and saque <= limite:
               saldo = saldo - saque
               numero_saques = numero_saques + 1 
               print("Saque realizado")
               extrato= f"Saque de: R${saque: .2f}"
            else:
                print("Sem saldo na conta")   

    elif opcao == "e":  
        print(extrato) 

    elif opcao == "q":
        print("Saindo")    
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação.")