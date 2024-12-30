class Animal:

    def __init__(self, nome):
        self.nome = nome

        variavel = "Valor"
        print(variavel)
    
    def comendo(self, alimento):
        return f"{self.nome} esta comendo {alimento}"
    
    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)
    


leao = Animal("Leao")
print(leao.nome)
print(leao.comendo("Carne"))

print(leao.executar("Carne"))