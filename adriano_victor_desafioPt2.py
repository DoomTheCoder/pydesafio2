##Desafio parte 2
##Definindo funções
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
[c] Criar Usuário

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
quantidade_de_saques_diarios_realizados = 0
historico_de_depositos = []
historico_de_saques = []
usuarios = []

def depositar(valor,/):
    deposito = valor
    if deposito > 0:
        historico_de_depositos.append(deposito)
        print(f" Seu saldo no valor de R${deposito:.2f} foi depositado")
        return deposito
    else:
        print("Valor de depósito inválido, por favor, tente novamente")
        return 0
    
def sacar(saque, limite, qtd_saques_realizados, max_saques_diarios, saldo):
    if saque <= limite and qtd_saques_realizados < max_saques_diarios:
            if saldo - saque >= 0:
                historico_de_saques.append(saque)
                global quantidade_de_saques_diarios_realizados
                quantidade_de_saques_diarios_realizados += 1
                print(f"Você sacou R${saque:.2f} com sucesso!")
                return saque
            else:
                print("Não foi possível realizar o saque, saldo insuficiente")
    else:
        print("operação inválida, limite de saques ou quantidade de saque acima do permitido, tente novamente")
    return 0

def extrato(depositos,/,*,saques):
    for item in depositos:
        print(f"Seus depósitos recentes foram: R${item:.2f}" )
    for item in saques:
        print(f"Seus saques recentes foram: R${item:.2f}")
    print(f"Seu saldo atual é: R${saldo:.2f}")


def criar_usuario():
    logradouro = ""
    num_da_casa = ""
    bairro = ""
    cidade = ""
    sigla_estado = ""
    print("Digite o nome do Usuário: ")
    usuario = {"nome" : input()}
    print("Digite a data de nascimento do usuário: ")
    usuario.update({"data de nascimento" : input()})
    print("Digite o CPF do usuário (Somente números): ")
    usuario.update({"CPF" : input()})
    print("Digite o logradouro do endereço: ")
    logradouro = input()
    print("Digite o numero da casa: ")
    num_da_casa = input()
    print("Digite o bairro: ")
    bairro = input()
    print("Digite a cidade: ")
    cidade = input()
    print("Digite a sigla do estado: ")
    sigla = input()
    endereco = f"{logradouro}, {num_da_casa} - {bairro} - {cidade}/{sigla}"
    usuario.update({"endereço" : endereco})
    usuarios.append(usuario)
    print(usuarios)

def criar_conta_corrente():
    pass

###Execução do programa###

while True:

    opcao = input(menu)

    if opcao[-1].lower() == "d":
        print("Digite um valor para depósito")
        valor_deposito = float(input())
        saldo += depositar(valor_deposito)
        


    elif opcao[-1].lower() == "s":
        print("Digite um valor para saque, máximo R$500,00 por saque")
        valor_de_saque = float(input())
        saldo -= sacar(saldo = saldo,saque = valor_de_saque, limite = limite, qtd_saques_realizados = quantidade_de_saques_diarios_realizados, max_saques_diarios= LIMITE_SAQUES)
        


    elif opcao == "e" or opcao[-1].lower() == "e":
        extrato(historico_de_depositos, saques = historico_de_saques)

    elif opcao[-1].lower() == "c":
        criar_usuario()

    elif opcao[-1].lower() == "q":
        print("Operação encerrada, obrigado por usar nosso sistema!")
        break
    
    else:
        print("Operação inválida, por favor, selecione novamente a operação desejada!")



    





