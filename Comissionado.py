from Funcionario import Funcionario 

class Comissionado(Funcionario):

    vendas:int

    def __init__(self, cod, nome, valorHora, horasTrabalhadas, vendas):
        super().__init__(cod, nome, valorHora, horasTrabalhadas) 
        self.vendas = vendas      
        self.salario = self.calcularSalario()
        
    def calcularSalario(self):
        salario = self.valorHora*self.horasTrabalhadas
        return salario*1.15
    
    def exibirComissionado(self):
        print(f"==== Funcionario Comissionado ====")
        print(f"Código: {self.cod} \nNome: {self.nome} \nValor de horas: {self.valorHora} \nHoras Trabalhadas: {self.horasTrabalhadas} \nVendas: {self.vendas} \nSalário: {self.salario:.1f}")

