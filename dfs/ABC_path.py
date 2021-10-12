import sys
import numpy as np

def position(char):
  '''
  Função que recebe um caracter e retorna o seu valor de posição. Por exemplo:
  A está na posição 1
  B está na posição 2
  e assim por diante...
  '''
  return ord(char) - 64

def prox_letra(i,j,x,y):
  '''
  Função que faz a verificação se a letra na posição de coordenadas i e j é uma letra anterior à letra
  na posição de coordenadas x e y.
  '''
  return position(grid[j][i]) == position(grid[y][x]) + 1

def check(x,y,W,H):
  '''
  Função que checa se as coordenadas x e y estão dentro dos limites do grid. Retorna o valor lógico.

  input:
    coordenadas x e y
    H - número de linhas, ou altura do grid
    W - número de colunas, ou largura do grid
  '''
  return (y >= 0 and y < H and x >= 0 and x < W)

def dfs(coord, visit, H, W):
  '''
  função que aplica o algoritmo DFS para cada letra 'A'. É uma função recursiva que vai atualizando a matriz visit cada vez que encontramos uma letra
  que possibilite um movimento válido. Movimentos válidos são sequências das letras, por exemplo: de 'A' para 'B', de 'D' para 'E'...
  
  input:
    coord - coordenadas da letra 'A'
    visit - simula uma matriz que marca se uma posição específica do grid já foi visitada ou não.
            Ela carrega 0 para não visitada. Para coordenadas já visitadas, ela informa o número da contagem de passos.
    H - número de linhas, ou altura do grid
    W - número de colunas, ou largura do grid
    
  obs.: a função não tem retorno nenhum, ela é usada somente para modificar a variável visit
  '''
  movs = {'x':[0,0,1,1,1,-1,-1,-1], 'y':[ 1,-1, 0, 1,-1, 0, 1,-1]}  # dicionário contendo as possibilidades de movimentos para x e y, incluindo diagonais
  x,y = coord       # x e y recebem as primeiras coordenadas, onde se encontra a letra 'A'
  for k in range(8):      # realizando todos os movimentos possíveis e verificando se é um movimento válido
    i = x + movs['x'][k]
    j = y + movs['y'][k]
    if (check(i,j,W,H)):
      if (visit[j][i] == 0 and prox_letra(i,j,x,y)):
        visit[j][i] += visit[y][x] + 1    # atualiza o número de passos na coordenada visitada
        dfs((i,j), visit, H, W)

# início do programa
        
n_case = 0    # iniciando o contador do número de casos

while (True):    # loop infinito até que W e H sejam 0
  
  H, W = [int(i) for i in sys.stdin.readline().split(' ')]

  if (H == 0 and W == 0):
    break

  else:

    n_case += 1
    # começando o teste:
    grid = []     # grade com as letras
    coord_A = []  # lista que armazena as coordenadas das letras 'A'
    visit = [[0]*W for i in range(H)]    # matriz que indica se as coordenadas das letras foram visitadas ou não

    for l in range(H):            # percorre as linhas
      grid.append(sys.stdin.readline())
      for c in range(W):          # percorre as colunas
        if (grid[l][c] == 'A'):   
          coord_A.append((c,l))   # armazenando as coordenadas de cada letra 'A'

    if (not coord_A):   # caso não for encontrado nenhuma letra A, nem precisamos chamar DFS
      print(f'Case {n_case}: 0')

    else:
      for coord in coord_A:   # aplicando a função dfs para cada letra 'A'
        visit[coord[1]][coord[0]] = 1   # colocando a primeira coordenada como visitada
        dfs(coord, visit, H, W)  
      
      print(f'Case {n_case}: {np.asarray(visit).max()}')  # a resposta que queremos é o maior valor do número de passos
