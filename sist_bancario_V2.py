

def menu():
   menu = """\n

   ========-Menu-=========

   [1]\t Depositar
   [2]\t Saque
   [3]\t Extrato
   [5]\t Nova Conta
   [6]\t Novo Cliente
   [7]\t Listar Contas
   [0]\t Sair

   ========-Fim Menu-======
   => """
   return input((menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Deposito realizado.")

    else:
        print("Operação não realizada! O valor informado é invalido.")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
       print("Operação não realizada! Você não tem saldo suficiente na conta.")

    elif excedeu_limite:
       print("Operação não realizada! Numero de saques excedido.")

    elif excedeu_saques:
       print("Operação não realizada! Quantidade maxima de saques excedidas.")

    elif valor > 0:
         saldo -= valor
         extrato += f"Saque: R$ {valor:.2f}\n"
         numero_saques += 1
         print("Saque realizado.")

    else:
       print("Operação não realizada! O Valor informado é invalido.")

    return saldo, extrato

def exibir_extrato(saldo,/, *, extrato):
     print("\n=============== Extrato ===============")
     print("Ainda não há movimentações na conta." if not extrato else extrato)
     print(f"\nSaldo: R$ {saldo:.2f}")
     print("=========================================")

def criar_novo_cliente(clientes):
    cpf = input("Informe seu CPF (Apenas numeros): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("Já existe uma conta para esse CPF.")
        return
    
    nome = input("Informe seu nome completo: ")
    data_de_nascimento = input("Informe sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o seu endereço (logradouro, n° - bairro - cidade/UF): ")

    clientes.append({"nome":nome, "dt_nasc":data_de_nascimento, "endereço":endereco, "CPF":cpf})
    print("Cliente cadastrado com sucesso!")

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente["cpf"] == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def criar_conta(agencia, numero_conta, clientes):
    cpf = input("Informe o CPF: ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("Sua conta foi criada com sucesso.")
        return {"agencia": agencia, "numero_conta":numero_conta, "cliente":cliente}
    
    print("Cliente não foi encontrado, veja se o processo está correto! ")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agencia:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['cliente']['nome']}
         """
    print("=" * 100)
    print((linha))

def main():
        LIMITE_SAQUES = 3
        AGENCIA = "0001"

        saldo = 0
        limite = 500
        extrato = ""
        numero_saques = 0
        clientes = []
        contas = []

        while True:
            opcao = menu()

            if opcao == "1":
                valor = float(input("Informe o valor para deposito: "))

                saldo, extrato = depositar(saldo,valor,extrato)

            elif opcao == "2":
                  valor = float(input("Informe o valor do saque: "))

                  saldo, extrato = sacar(
                      saldo=saldo,
                      valor=valor,
                      extrato=extrato,
                      limite=limite,
                      numero_saques=numero_saques,
                      limite_saques=LIMITE_SAQUES,
                  )

            elif opcao == "3":
                exibir_extrato(saldo, extrato=extrato)

            elif opcao == "5":
                criar_novo_cliente(clientes)

            elif opcao == "6":
                numero_conta = len(contas) + 1
                conta = criar_conta(AGENCIA,numero_conta,clientes)

                if conta:
                    contas.append(conta)

            elif opcao == "7":
                listar_contas(contas)

            elif opcao == "0":
                break

            else:
                print("Operação invalida, Selecione corretamente e continue a operação.")

main()




         
    

