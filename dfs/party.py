import sys

def dfs(temp, grafos, visit, i):
  '''
  função dfs recursiva que modifica a variável n_grupos, para dizer qual a contagem mínima de grupos que
  pode ser formada no problema. Aqui se entende que esse número é igual ao maior ramo dos grafos.

  input:
    temp = variável temporária, que altera a cada novo elemento que se percorre nos ramos. Quanto mais 
           distante o elemento for do início do ramo, maior vai ser temp. O valor máximo de temp que for
           encontrado, armazenaremos na variável global n_grupos.
    grafos = lista contendo para cada elemento (empregado), os subordinados diretos daquele elemento. Se
             ele não tiver nenhum subordinado, aquele índice apresentará uma lista vazia.
    visit = lista de quais empregados (elementos) já foram visitados pelo dfs
    i = índice atual ao qual o dfs está percorrendo
  '''

  global n_grupos   # declarando n_grupos como variável global
  visit[i] = 1    # marcando como visitado
  for v in grafos[i]:   # percorrendo todos os dubordinados diretos de i
    if (visit[v] == 0):
      temp += 1
      if (temp > n_grupos):   # assim garantimos que n_grupos será o número de elementos do maior ramo -1
        n_grupos = temp
      dfs(temp, grafos, visit, v)
      temp -= 1

# iniciando o teste
n = int(sys.stdin.readline())
managers = []   # lista contendo quem é o chefe imediato de cada empregado
grafos = [[] for i in range(n)]
visit = [0 for i in range(n)]
global n_grupos
n_grupos = 0    # número mínimo de grupos que precisamos formar. será aumentado nas iterações do bfs

for i in range(n):
  managers.append(int(sys.stdin.readline())-1)

for i in range(n):
  if (managers[i] != -2):
    grafos[managers[i]].append(i)

for i in range(n):
  if (managers[i] == -2):     # chamando o algoritmo dfs para cada ínicio de ramo
    dfs(0, grafos, visit, i)

# retornando o número mínimo de grupos que precisamos formar
print(n_grupos + 1)
