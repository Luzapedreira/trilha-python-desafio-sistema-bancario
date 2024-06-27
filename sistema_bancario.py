import datetime

class Cliente:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco

class ContaBancaria:
    numero_conta_sequencial = 1
    
    def __init__(self, cliente):
        self.cliente = cliente
        self.agencia = "0001"
        self.numero_conta = ContaBancaria.numero_conta_sequencial
        ContaBancaria.numero_conta_sequencial += 1
        self.saldo = 0.0
        self.limite_saque_diario = 500.0
        self.limite_saques_mensais = 3
        self.saques_realizados = 0
        self.extrato = []

    def depositar(self, saldo, valor, extrato):
        if valor > 0:
            saldo += valor
            extrato.append(f"Depósito: R$ {valor:.2f}")
            return saldo, extrato
        else:
            print("Valor de depósito inválido.")
            return saldo, extrato

    def sacar(self, *, saldo, valor, extrato, limite, numero_saques, limite_saques):
        if valor <= 0:
            print("Valor de saque inválido.")
        elif valor > saldo:
            print("Saldo insuficiente.")
        elif valor > limite:
            print("Valor de saque excede o limite diário de R$ 500,00.")
        elif numero_saques >= limite_saques:
            print("Número de saques mensais excedido.")
        else:
            saldo -= valor
            numero_saques += 1
            extrato.append(f"Saque: R$ {valor:.2f}")
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        return saldo, extrato, limite, numero_saques, limite_saques

    def verificar_extrato(self, saldo, *, extrato):
        print("\nExtrato Bancário:")
        for item in extrato:
            print(item)
        print(f"Saldo atual: R$ {saldo:.2f}\n")

def cadastrar_usuario(usuarios):
    nome = input("Digite o nome do cliente: ")
    data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
    cpf = input("Digite o CPF (apenas números): ")
    endereco = input("Digite o endereço (logradouro, número - bairro - cidade/sigla do estado): ")

    for usuario in usuarios:
        if usuario.cpf == cpf:
            print("CPF já cadastrado. Cadastro não realizado.")
            return usuarios

    novo_usuario = Cliente(nome, data_nascimento, cpf, endereco)
    usuarios.append(novo_usuario)
    print(f"Cliente {nome} cadastrado com sucesso!")
    return usuarios

def cadastrar_conta(contas, usuarios):
    cpf = input("Digite o CPF do cliente para vincular a conta: ")
    
    for usuario in usuarios:
        if usuario.cpf == cpf:
            nova_conta = ContaBancaria(usuario)
            contas.append(nova_conta)
            print(f"Conta {nova_conta.numero_conta} cadastrada com sucesso para o cliente {usuario.nome}!")
            return contas
    
    print("CPF não encontrado. Conta não cadastrada.")
    return contas

def main():
    usuarios = []
    contas = []

    while True:
        print("\nMenu Principal")
        print("1. Cadastrar Usuário")
        print("2. Cadastrar Conta")
        print("3. Acessar Conta")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            usuarios = cadastrar_usuario(usuarios)
        elif opcao == "2":
            contas = cadastrar_conta(contas, usuarios)
        elif opcao == "3":
            cpf = input("Digite o CPF do cliente para acessar a conta: ")
            conta = next((conta for conta in contas if conta.cliente.cpf == cpf), None)
            if conta:
                while True:
                    print("\nMenu da Conta")
                    print("1. Depositar")
                    print("2. Sacar")
                    print("3. Verificar Extrato")
                    print("4. Voltar ao Menu Principal")
                    opcao_conta = input("Escolha uma opção: ")

                    if opcao_conta == "1":
                        valor = float(input("Digite o valor para depósito: "))
                        conta.saldo, conta.extrato = conta.depositar(conta.saldo, valor, conta.extrato)
                    elif opcao_conta == "2":
                        valor = float(input("Digite o valor para saque: "))
                        conta.saldo, conta.extrato, conta.limite_saque_diario, conta.saques_realizados, conta.limite_saques_mensais = conta.sacar(
                            saldo=conta.saldo, valor=valor, extrato=conta.extrato, limite=conta.limite_saque_diario, 
                            numero_saques=conta.saques_realizados, limite_saques=conta.limite_saques_mensais
                        )
                    elif opcao_conta == "3":
                        conta.verificar_extrato(conta.saldo, extrato=conta.extrato)
                    elif opcao_conta == "4":
                        break
                    else:
                        print("Opção inválida. Tente novamente.")
            else:
                print("CPF não encontrado.")
        elif opcao == "4":
            print("Obrigado por usar o sistema bancário!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
