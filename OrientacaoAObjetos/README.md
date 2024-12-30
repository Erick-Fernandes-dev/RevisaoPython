
# Class em python
---

- As classes geram novos Objetos (instâncias) que podem ter seus próprios atributos e métodos.

- Os objetos gerados pela classe podem usar seus dados internos para realizar várias ações.

- Por convenção, usamos PascalCase para nomes de classes

---
# Self

- Na classe o sel é a própria instancia

```python
class Carro:
    def __init__(self, nome):
        self.nome = nome
    
    def acelerar(self):
        print(f"{self.nome}, esta acelerando")

fusca = Carro("Fusca")
print(fusca.nome)
fusca.acelerar()

ferrari = Carro("Ferrari")
print(ferrari.nome)
ferrari.acelerar()
```

---
# Escopo
---

```python
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
```

--- 
# Mantendo o estado dentro da classe
---

```python
class Camera:

    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando
    
    def filmar(self):

        if self.filmando:
            print(f"{self.nome} ja esta filmando")
            return


        print(f"{self.nome} esta filmando")
        self.filmando = True
    
    def parar_filmar(self):
        if not self.filmando:
            print(f"{self.nome} não está filmando")
            return
        
        print(f"{self.nome} parou de filmar")
        self.filmando = False
    
    def fotografar(self):
        if self.filmando:
            print(f"{self.nome} não pode fotografar enquanto esta filmando")
            return

        print(f"{self.nome} esta fotografando")


c1 = Camera("Canon")
c2 = Camera("Sony")


c1.filmar()
c1.filmar()
c1.fotografar()
c1.parar_filmar()
c1.parar_filmar()
c1.fotografar()

print("\n")

c2.filmar()
c2.filmar()
c2.fotografar()
c2.parar_filmar()
c2.parar_filmar()
c2.fotografar()

```

---

# Hard Code

---

**Hard code** (ou **hardcoding**) é uma prática de programação em que valores ou comportamentos específicos são diretamente escritos no código-fonte, em vez de serem parametrizados ou extraídos de fontes externas, como arquivos de configuração, bancos de dados, ou variáveis de ambiente.

### Exemplos de Hard Code

1. **Hard code de valores fixos:**
   ```python
   taxa_desconto = 0.1  # Valor fixo no código
   preco_final = preco_original * (1 - taxa_desconto)
   ```
   Aqui, o desconto de 10% está embutido no código. Se precisar ser alterado, o programador terá que modificar o código diretamente.

2. **Hard code de strings ou caminhos:**
   ```python
   caminho_arquivo = "C:/projeto/config.txt"
   ```
   Se o programa precisar rodar em outro ambiente, o caminho terá que ser alterado manualmente.

---

### Problemas com Hard Code
1. **Dificuldade de manutenção:** Alterar o valor exige mudanças no código, podendo introduzir erros.
2. **Falta de flexibilidade:** O software não se adapta facilmente a novos requisitos ou ambientes.
3. **Risco de segurança:** Hard code de senhas ou chaves de API pode expor informações sensíveis.

---

### Melhor Alternativa
Em vez de usar hard code, pode-se optar por:

- **Arquivos de configuração:**
  ```python
  import configparser
  config = configparser.ConfigParser()
  config.read("config.ini")
  taxa_desconto = float(config["DESCONTO"]["taxa"])
  ```
- **Variáveis de ambiente:**
  ```python
  import os
  taxa_desconto = float(os.getenv("TAXA_DESCONTO", 0.1))
  ```
- **Parâmetros ou argumentos:**
  Passar valores como argumentos na linha de comando ou via métodos/funções.

Adotar essas práticas promove um código mais limpo, reutilizável e fácil de manter.
---
# Atributos de classe
---

```python
class Pessoa:

    ano_atual = 2024


    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade

p1 = Pessoa("Erick", 19)
p2 = Pessoa("Maria", 20)

print(Pessoa.ano_atual)
#Pessoa.ano_atual = 1

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
```

