import sys

def check(y,x,n,m):
  return (y >= 0 and y < n and x >= 0 and x < m)

def test(n, m):

  # iniciando variáveis
  mark = [[-1]*m for i in range(n)]
  movs = {'y':[1,-1,0,0], 'x':[0,0,1,-1]}
  fila = []

  # começando o programa
  fila.append((0,0))  # cada elemento da fila é uma tupla com as coordenadas
  mark[0][0] = 0    # começamos com o passo de número 0 no canto superior esquerdo
  sz = 1
  pos = 0

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
