
saldo = 0
extrato = []
limite_por_saque = 500
numero_saques = 0 
LIMITE_DE_SAQUES = 3

# Função de Menu
def menu():
    # Loop principal do Sistema
    while True :
        
        texto_menu = f"""
        --------------------------------------
        Bem-vindo ao Caixa Eletrônico
        --------------------------------------
        Seu Saldo atual é: R$ {saldo:,.2f}

        Opções (digite a letra):
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair
        """

        opcao = input(texto_menu).strip().lower()

        if opcao == "d":
            depositar()

        elif opcao == "s":
            sacar()

        elif opcao == "e":
            mostrar_extrato()
        
        elif opcao == "q":
            print("Encerrando até logo!")
            break

        else:
            print("Operação inválida. Tente novamente. \n")

# Função de deposito

def depositar():

    global saldo,extrato

    menu_deposito = """ 
    Você entrou na área de Depósito.
    Deseja continuar?

    [y] Sim
    [n] Não
    """

    while True:
        opcao = input(menu_deposito).strip().lower()

        if opcao == "y":
            valor_txt = input("Quanto deseja depositar? (Insira só numeros inteiros)\n")

            if not valor_txt.isdigit():
                print("Valor inválido. Digite apenas números inteiros positivos.\n")
                continue
            
            deposito = int(valor_txt)

            if deposito <= 0:
                print("O valor do depósito deve ser maior que zero \n")
                continue

            print("Insira as cédulas no caixa eletrônico...")

            saldo += deposito
            extrato.append({"tipo": "depósito", "valor": deposito})

            print(f"Parabéns! Você depositou R$ {deposito:,.2f} e seu saldo atual é de R$ {saldo:,.2f}\n ")
            return
        elif opcao == "n":
            print("Voltando ao menu principal...\n")
            return
        
        else:
            print("Opção inválida. Por favor, digite y ou n. \n")


def sacar():

    global saldo,extrato,limite_por_saque,LIMITE_DE_SAQUES,numero_saques

    menu_saque = """ 
    Você entrou na área de Saque.
    Deseja continuar?

    [y] Sim
    [n] Não
    """
    while True:
        opcao = input(menu_saque).strip().lower()

        if opcao == "y":

            if numero_saques > LIMITE_DE_SAQUES:
                print("Você atingiu o limite diário de saque")
                return


            valor_txt = input("Quanto deseja sacar? (Insira só numeros inteiros)\n")

            if not valor_txt.isdigit():
                print("Valor inválido. Digite apenas números inteiros positivos.\n")
                continue
            
            saque = int(valor_txt)

            if saque <= 0:
                print("O valor do saque deve ser maior que zero \n")
                return

            if saque > saldo:
                print("Você não tem saldo suficiente. Tente um valor menor\n")
                return

            if saque > limite_por_saque:
                print("O limite diário de saque é de R$: {limite_por_saque:.2f}.\n")
                return
            
            saldo -= saque
            numero_saques += 1
            extrato.append({"tipo": "saque", "valor": saque})

            print(f"Saque de R$ {saque:.2f} realizado com sucesso!")
            print(f"Saldo atual: R$ {saldo:.2f}\n")

        elif opcao == "n":
            print("Voltando ao menu principal...\n")
            return
        
        else:
            print("Opção inválida. Por favor, digite y ou n. \n")


def mostrar_extrato():

    global extrato,saldo

    menu_extrato = """ 
    Você entrou na área do Extrato.
    Deseja continuar?

    [y] Sim
    [n] Não
    """
    while True:
        opcao = input(menu_extrato).strip().lower()


        if opcao == "y":
            print("\n========== EXTRATO ==========")

            if len(extrato) == 0:

                print("Não foram realizadas movimentações.")
            
            else:
                for op in extrato:
                    print(f"{op['tipo'].capitalize()}: R$ {op['valor']:.2f}")

            print(f"Saldo atual: R$ {saldo:.2f}")
            print("==============================\n")

        elif opcao == "n":
            print("Voltando ao menu principal...\n")
            return
        
        else:
            print("Opção inválida. Por favor, digite y ou n. \n")           


        
    







menu()




