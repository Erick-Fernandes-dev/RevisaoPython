Esse código implementa uma **MinHeap**, uma estrutura de dados semelhante à MaxHeap, mas com a propriedade de que o menor elemento sempre está no topo (raiz). Aqui está uma explicação detalhada do funcionamento da implementação:

---

### **1. O que é uma MinHeap?**
- Uma **MinHeap** é uma árvore binária completa onde:
  - O valor de cada nó é menor ou igual aos valores de seus filhos.
  - O menor elemento está no topo.

Exemplo:
```
        3
      /   \
     4     6
    / \
   10  5
```

---

### **2. Estrutura da Classe `MinHeap`**

#### **Atributos**
- `heap_list`: Lista usada para representar a MinHeap. O índice `0` não é utilizado.
- `current_size`: Número de elementos atualmente na heap.

---

### **3. Métodos da Classe**

#### **Construtor (`__init__`)**
```python
def __init__(self):
    self.heap_list = [0]  # Índice 0 não usado, facilita cálculos de pai/filhos
    self.current_size = 0  # Tamanho inicial da heap
```

#### **Subir um Elemento (`sift_up`)**
```python
def sift_up(self, i):
    stop = False
    while (i // 2 > 0) and stop == False:
        if self.heap_list[i] < self.heap_list[i // 2]:
            self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
        else:
            stop = True
        i = i // 2
```
- Move o elemento na posição `i` para cima, comparando-o com seu pai.
- Para manter a propriedade da MinHeap, troca o elemento com seu pai se ele for menor.

---

#### **Inserir um Elemento (`insert`)**
```python
def insert(self, k):
    self.heap_list.append(k)  # Adiciona o elemento ao final da lista
    self.current_size += 1    # Incrementa o tamanho
    self.sift_up(self.current_size)  # Ajusta a posição do elemento com `sift_up`
```
- Adiciona um elemento à MinHeap.
- Ajusta sua posição para manter a propriedade de MinHeap.

---

#### **Descer um Elemento (`sift_down`)**
```python
def sift_down(self, i):
    while (i * 2) <= self.current_size:  # Enquanto houver um filho esquerdo
        mc = self.min_child(i)  # Obtém o menor filho
        if self.heap_list[i] > self.heap_list[mc]:
            self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
        i = mc
```
- Move o elemento na posição `i` para baixo, comparando-o com seus filhos.
- Se o elemento for maior que o menor de seus filhos, troca suas posições.

---

#### **Encontrar o Menor Filho (`min_child`)**
```python
def min_child(self, i):
    if (i * 2) + 1 > self.current_size:  # Se não há filho direito
        return i * 2  # Retorna o filho esquerdo
    else:  # Se há ambos os filhos
        if self.heap_list[i * 2] < self.heap_list[(i * 2) + 1]:
            return i * 2  # Retorna o menor filho (esquerdo)
        else:
            return (i * 2) + 1  # Retorna o menor filho (direito)
```
- Determina o menor filho de um nó para ser usado em `sift_down`.

---

#### **Remover o Menor Elemento (`delete_min`)**
```python
def delete_min(self):
    if len(self.heap_list) == 1:  # Se a heap está vazia
        return 'Empty heap'

    root = self.heap_list[1]  # Menor elemento (raiz)

    self.heap_list[1] = self.heap_list[self.current_size]  # Substitui a raiz pelo último elemento

    *self.heap_list, _ = self.heap_list  # Remove o último elemento

    self.current_size -= 1  # Decrementa o tamanho

    self.sift_down(1)  # Ajusta a heap usando `sift_down`

    return root  # Retorna o menor elemento removido
```
- Remove e retorna o menor elemento (raiz).
- Ajusta os elementos restantes para manter a propriedade de MinHeap.

---

### **4. Exemplo de Uso**
```python
m = MinHeap()
m.insert(10)
m.insert(5)
m.insert(6)
m.insert(3)
m.insert(4)

print(m.heap_list)           # [0, 3, 4, 6, 10, 5]
print(m.delete_min())        # 3 (menor elemento removido)
print(m.heap_list)           # [0, 4, 5, 6, 10]
print(m.delete_min())        # 4 (menor elemento removido)
print(m.heap_list)           # [0, 5, 10, 6]
```

---

### **Explicação do Comportamento**
1. **Inserção:**
   - Os elementos são adicionados e organizados para que o menor valor fique na raiz.
   - Estrutura após as inserções: `[0, 3, 4, 6, 10, 5]`.

2. **Remoção (delete_min):**
   - Remove o menor elemento (raiz) e substitui pela última folha.
   - Ajusta a heap para manter a propriedade.
   - Após remover `3`: `[0, 4, 5, 6, 10]`.
   - Após remover `4`: `[0, 5, 10, 6]`.

---

### **Resumo**
- **MinHeap** mantém o menor elemento sempre na raiz.
- Métodos principais:
  - **`insert`**: Adiciona elementos mantendo a ordem.
  - **`delete_min`**: Remove o menor elemento.
- Métodos auxiliares (`sift_up`, `sift_down`, `min_child`) garantem a propriedade da MinHeap.