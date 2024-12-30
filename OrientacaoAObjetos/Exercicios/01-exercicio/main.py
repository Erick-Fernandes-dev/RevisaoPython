# Exercicio - Salve sua classe em json 
# Salve os dados da sua classe em json
# e depois crie novamente as instancias
# da classe com os dados do json
# Faça em arquivos separados


import json
from loguru import logger

class Biblioteca:


    def __init__(self, nome, ano, autor):
        self.nome = nome
        self.ano = ano
        self.autor = autor
    

# Salvar em json
def salvar_em_json(obj, arquivo):
    with open(arquivo, "w") as file:
        json.dump(vars(obj), file)
    logger.debug("Objeto salvo com sucesso")
    

# Função para ler o arquivo json
def ler_arquivo_json(arquivo):
    with open(arquivo, "r") as f:
        dados = json.load(f)
        return Biblioteca(**dados)

# Usando as funções
l1 = Biblioteca("Aprendendo Python", 2020, "Erick Wendel")
salvar_em_json(l1, "biblioteca.json")


# Carregando o arquivo json
l2 = ler_arquivo_json("biblioteca.json")
print(l2.nome, l2.ano, l2.autor)


    

