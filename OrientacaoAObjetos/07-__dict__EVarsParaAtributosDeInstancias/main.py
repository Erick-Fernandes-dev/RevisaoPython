class Pessoa:

    ano_atual = 2024


    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
dados = {'nome': 'Erick', 'idade': 19}


p1 = Pessoa(**dados) # nome="Erick", idade=19
p2 = Pessoa("Maria", 20)

print(Pessoa.ano_atual)
#Pessoa.ano_atual = 1

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())

print(p1.__dict__)
print(vars(p1))

#p1.__dict__["nome"] = "Erick"
#print(p1.__dict__)
#p1.__dict__["outra"] = "Coisa"
#print(p1.__dict__.get("outra"))
#p1.__dict__["nome"] = "EITA"
#del p1.__dict__["outra"]
#print(p1.__dict__)