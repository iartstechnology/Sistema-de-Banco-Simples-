class Banco:
    def __init__(self):
        self.saldo = 0
        self.depositos = []
        self.saques = []
        self.saques_diarios = 0

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(f"Depósito de R${valor:.2f}")
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("Erro: Valor de depósito inválido. Somente valores positivos são permitidos.")

    def saque(self, valor):
        if self.saldo >= valor and self.saques_diarios < 3:
            self.saldo -= valor
            self.saques.append(f"Saque de R${valor:.2f}")
            self.saques_diarios += 1
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
        elif self.saldo < valor:
            print("Erro: Saldo insuficiente. Não é possível sacar o dinheiro.")
        else:
            print("Erro: Limite de saques diários atingido. Tente novamente amanhã.")

    def extrato(self):
        print("Extrato da conta:")
        for deposito in self.depositos:
            print(deposito)
        for saque in self.saques:
            print(saque)
        print(f"Saldo atual: R${self.saldo:.2f}")

banco = Banco()

while True:
    print("Opções:")
    print("1. Depósito")
    print("2. Saque")
    print("3. Extrato")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor = float(input("Digite o valor do depósito: "))
        banco.deposito(valor)
    elif opcao == "2":
        valor = float(input("Digite o valor do saque: "))
        banco.saque(valor)
    elif opcao == "3":
        banco.extrato()
    elif opcao == "4":
        break
    else:
        print("Opção inválida. Tente novamente.")
