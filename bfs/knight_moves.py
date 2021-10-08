import sys

def check(y,x):
  '''
  checa se as coordenadas x e y estão dentro dos limites de casas do tabuleiro de xadrez, onde cada lado vai dos números 1 ao 8.
  
  input: 
    y - coordenada y
    x - coordenada x
   
   retorna o valor lógico da operação
  '''
  return (y >= 0 and y < 8 and x >= 0 and x < 8)

def test(inicio, fim):
  '''
  função que realiza cada teste solicitado.
  Aqui usamos uma lista python para simular uma fila. A cada iteração, chamamos o próximo elemento da lista, que é como se estivessemos excluindo o primeiro elemento
  de uma fila. O objeto fila é portanto uma lista, mas que funciona como uma fila. Nesse objeto guardamos todas as coordenadas que passamos realizando os movimentos.
  Para simular uma matriz, foi usado lista de listas. Por exemplo, o objeto mark é uma lista de listas que funciona como matriz. Ao acessarmos mark[l][c] estamos acessando
  na verdade o c-ésimo elemento da l-ésima lista, mas podemos pensar que estamos acessando o elemento de linha l e coluna c.
  
  input:
    inicio - recebe as coordenadas da primeira casa aonde o cavalo está
    fim - recebe as coordenadas de onde o cavalo deve chegar
    
  return:
    retorna o número de passos que foram necessários para o cavalo chegar à posição final. Em outras palavras retorna mark[x][y] onde x e y são as coordenadas do destino
    final.
  '''
  
  # iniciando variáveis
  mark = [[-1]*8 for i in range(8)]     # matriz para indicar quais posições já foram visitadas e qual o número do passo em cada uma delas
  movs = {'y':[ 2, 2,-2,-2, 1, 1,-1,-1], 'x':[ 1,-1, 1,-1, 2,-2, 2,-2]}   # dicionário usado para realizar os movimentos de um cavalo no xadrez. são 8 possibilidades
  fila = []                             # lista que funciona como fila
  
  # começando o programa de fato
  fila.append(inicio)  # cada elemento da fila é uma tupla com as coordenadas
  mark[inicio[1]][inicio[0]] = 0    # começamos com o passo de número 0 nas coordenadas de inicio
  sz = 1               # tamanho inicial da fila
  pos = 0              # posição inicial solicitada da fila

  while (pos!=sz):
    x = fila[pos][1]
    y = fila[pos][0]
    pos += 1

    # verificamos se já estamos na última posição
    if (y == fim[0] and x == fim[1]):
      return mark[x][y]

    for k in range(8):
      i = x + movs['x'][k]
      j = y + movs['y'][k]

      if (check(i,j) and mark[i][j] == -1):
        mark[i][j] = mark[x][y] + 1
        fila.append((j,i))
        sz += 1

  return -1

map = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}    # dicionário para mapear as casas do tabuleiro como índices de uma matriz

# realizando todos os testes
for line in sys.stdin:
  i, f = line.replace('\n','').split(' ')
  inicio = (map[i[0]], int(i[1]) - 1)
  fim = (map[f[0]], int(f[1]) - 1)
  print('To get from', i, 'to', f, 'takes', test(inicio, fim), 'knight moves.')
