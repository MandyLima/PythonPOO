class Funcionario:

    cod:int
    nome:str
    valorHora:int
    horasTrabalhadas:int
    
    def __init__(self, cod, nome, valorHora, horasTrabalhadas):
        self.cod = cod
        self.nome = nome
        self.valorHora = valorHora
        self.horasTrabalhadas = horasTrabalhadas
        self.salario = self.calcularSalario()

    def calcularSalario(self):
        return self.valorHora*self.horasTrabalhadas
    
    def exibirFuncionario(self):
        print(f"Código: {self.cod} \nNome: {self.nome} \nValor de horas: {self.valorHora} \nHoras Trabalhadas: {self.horasTrabalhadas} \nSalário: {self.salario}")
        

fc1 = Funcionario (1, "Maria Clara",25, 30 ) 
fc1.exibirFuncionario() 
