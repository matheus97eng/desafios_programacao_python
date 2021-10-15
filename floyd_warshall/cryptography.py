import sys

def P(char):
  '''
  Função que recebe um caracter e retorna o seu valor na posição.
  ! está na posição 0
  " está na posição 1
  e assim por diante seguindo a tabela ASCII...
  '''
  return ord(char) - 33

def floyd_warshall(dist):  
  '''
  Algoritmo para encontrar o menor custo dado quaisquer 2 pontos.

  input: 
    dist - matriz de adjascência que carrega o custo de 'a' para 'b' onde
           'a' é a posição da linha da matriz e 'b' é a posição da coluna
  return:
    a matriz dist atualizada com os menores custos
  ''' 

  for k in range(100):
    for j in range(100):
      for i in range(100):
        dist[j][i] = min(dist[j][i], dist[j][k] + dist[k][i])
  return dist

def out(cod1, cod2, dist, inf):
  '''
  Função que gera a saída esperada do teste: a soma dos custos para alterar cada caracter da palavra cod1
  para cod2. Se não for possível fazer essa alteração (em outras palavras, se em qualquer das posições 
  o custo para trocar o caracter de cod1 para o caracter de cod2 for infinito) o retorno será -1.
  
  input: 
    cod1 - palavra a ser criptografada
    cod2 - palavra criptografada
    dist
    inf
  '''

  sum = 0   # inicializa a soma
  for iter in range(len(cod1)):   # percorrendo cada caracter das palavras armazenadas em cod1 e cod2
    if (dist[P(cod1[iter])][P(cod2[iter])] < inf):
      sum += dist[P(cod1[iter])][P(cod2[iter])]
    else:
      return -1
  return sum

# main
cod1 = input()    # primeira e segunda palavra
cod2 = input()

inf = len(cod1)*100000    # máximo valor de custo que pode haver entre 2 vértices 
dist = [100*[inf] for x in range(100)]    # preparando a matriz de adjacência
for iter in range(100):
  dist[iter][iter] = 0   # não há distância de um vértice pra ele mesmo

n = int(input())    # número de vezes que precisaremos ler os grafos
for iter in range(n):
  j, i, d = [x for x in input().split(' ')]   # custo d para sair de j para i, ou se preferir...
                                              # posição da coluna, linha e custo, respectivamente
  dist[P(j)][P(i)] = min(dist[P(j)][P(i)], int(d))

dist = floyd_warshall(dist)

print(out(cod1, cod2, dist, inf))
