string = "erick"

print(string.upper())# Maiusculo
print(string.lower())# Minusculo
print(string.capitalize())# Primeira letra maiuscula

class Pessoa:

    def __init__(self, nome, sobreNome):
        self.nome = nome
        self.sobreNome = sobreNome
    

p1 = Pessoa("Erick", "Santos")


p2 = Pessoa("Maria", "Silva")


