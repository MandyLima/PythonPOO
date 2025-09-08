from Funcionario import Funcionario
from Comissionado import Comissionado

def main():
    print("\n==== Cadastro de Funcionário Comum ====")
    cod = int(input("Código:"))
    nome = input("Nome:")
    valorHora = int(input("Valor da Hora: "))
    horasTrabalhadas = int(input("Horas trabalhadas: "))

    funcionario = Funcionario(cod, nome, valorHora, horasTrabalhadas)

    print("\n==== Dados do Funcionário Comum ====")
    funcionario.exibirFuncionario()


    print("\n==== Cadastro de Funcionário Comum ==== ")
    cod = int(input("Código:"))
    nome = input("Nome:")
    valorHora = int(input("Valor da Hora: "))
    horasTrabalhadas = int(input("Horas trabalhadas: "))
    vendas = int(input("Vendas feitas: "))

    comissionado = Comissionado (cod, nome, valorHora, horasTrabalhadas, vendas)

    print("\n==== Dados do Funcionário Comissionado ====")
    comissionado.exibirComissionado()

if __name__ == "__main__":
    main()