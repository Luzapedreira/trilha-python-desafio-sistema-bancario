class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.saldo = 0.0
        self.limite_saque_diario = 500.0
        self.limite_saques_mensais = 3
        self.saques_realizados = 0
        self.extrato = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor <= 0:
            print("Valor de saque inválido.")
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        elif valor > self.limite_saque_diario:
            print("Valor de saque excede o limite diário de R$ 500,00.")
        elif self.saques_realizados >= self.limite_saques_mensais:
            print("Número de saques mensais excedido.")
        else:
            self.saldo -= valor
            self.saques_realizados += 1
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

    def verificar_extrato(self):
        print("\nExtrato Bancário:")
        for item in self.extrato:
            print(item)
        print(f"Saldo atual: R$ {self.saldo:.2f}\n")

    def menu(self):
        while True:
            print("1. Depositar")
            print("2. Sacar")
            print("3. Verificar Extrato")
            print("4. Sair")
            opcao = input("Escolha uma opção: ")
            
            if opcao == "1":
                valor = float(input("Digite o valor para depósito: "))
                self.depositar(valor)
            elif opcao == "2":
                valor = float(input("Digite o valor para saque: "))
                self.sacar(valor)
            elif opcao == "3":
                self.verificar_extrato()
            elif opcao == "4":
                print("Obrigado por usar o sistema bancário!")
                break
            else:
                print("Opção inválida. Tente novamente.")

def main():
    nome_cliente = input("Digite o nome do cliente: ")
    cliente = Cliente(nome_cliente)
    cliente.menu()

if __name__ == "__main__":
    main()