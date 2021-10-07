import sys

def check(y,x,n,m):
  '''
  checa se as coordenadas x e y estão dentro do grid
  
  input: 
    y - coordenada y
    x - coordenada x
    n - limite de linhas
    m - limite de colunas
   
   retorna o valor lógico da operação
  '''
  return (y >= 0 and y < n and x >= 0 and x < m)

def test(n, m):
  '''
  função que realiza o teste do problema.
  Aqui usamos uma lista python para simular uma fila. A cada iteração, chamamos o próximo elemento da lista, que é como se estivessemos excluindo o primeiro elemento
  de uma fila. O objeto fila é portanto uma lista, mas que funciona como uma fila.
  Para simular uma matriz, foi usado lista de listas. Por exemplo, o objeto mark é uma lista de listas que funciona como matriz. Ao acessarmos mark[l][c] estamos acessando
  na verdade o c-ésimo elemento da l-ésima lista, mas podemos pensar que estamos acessando o elemento de linha l e coluna c.
  
  input:
    n - número de linhas
    m - número de colunas
    
  return:
    resposta do teste. -1 caso não seja possível se chegar ao final do grid. Caso seja possível, retorna o número de passos dados
  '''

  # iniciando variáveis
  mark = [[-1]*m for i in range(n)]         # matriz que indica quais posições foram visitadas e quantos passos foram dados para chegar nela
  movs = {'y':[1,-1,0,0], 'x':[0,0,1,-1]}   # dicionário usado para realizar os movimentos
  fila = []                                 # lista que funciona como fila

  # começando o programa
  fila.append((0,0))  # cada elemento da fila é uma tupla com as coordenadas
  mark[0][0] = 0    # começamos com o passo de número 0 no canto superior esquerdo
  sz = 1            # tamanho atual da fila
  pos = 0           # posição atual da fila

  while (pos!=sz):
    x = fila[pos][1]
    y = fila[pos][0]
    pos += 1

    # verificamos se já estamos na última posição
    if (y == n-1 and x == m-1):
      return mark[y][x]

    for k in range(4):
      i = y + int(mp[y][x])*movs['y'][k]
      j = x + int(mp[y][x])*movs['x'][k]

      if (check(i,j,n,m) and mark[i][j] == -1):
        mark[i][j] = mark[y][x] + 1
        fila.append((i,j))
        sz += 1

  return -1

n, m = [int(i) for i in sys.stdin.readline().split()]
mp = []
for l in range(n):
  mp.append(sys.stdin.readline())
print(test(n,m))
