from heapq import heappush, heappop

# condições:
inf = 10**11 + 1   # distância tem um limite de 10**5 * 10**6

def dijkstra(vizinhos, n):
  
  distancia = n*[inf]
  distancia[0] = 0
  caminhos = []
  processado = n*[False]

  fila = []
  heappush(fila, (distancia[0], 0, [1]))  # para o python o índice é 0
                                          # mas nosso caminho começa com 1
  
  menor_caminho = [[]]

  while (True):

    davez = -1
    while (fila):
      d, atual, caminho_atual = heappop(fila)
      if (not processado[atual]):
        davez = atual
        break
    
    if (caminho_atual[-1] == n):  
      if (d < distancia[-1]):           # se encontramos um novo menor caminho, atualizamos
        menor_caminho = [caminho_atual]
      if (d == distancia[-1]):          # se encontramos um menor caminho alternativo, acrescentamos
        menor_caminho.append(caminho_atual)
    if (davez == -1):   # se não há mais vértices para analisar podemos parar
      break

    processado[davez] = True
    
    # atualizando as distâncias
    for v in vizinhos[davez]:
      dist = v['peso']
      vizinho = v['vertice']
      # se a distância precisar ser atualizada, atualizamos a distância e a fila
      if (distancia[vizinho] > distancia[davez] + dist):
        distancia[vizinho] = distancia[davez] + dist
        heappush(fila, (distancia[vizinho], vizinho, caminho_atual + [vizinho+1]))
   
  return menor_caminho

import sys

n, m = [int(i) for i in sys.stdin.readline().split()]
vizinhos = [[] for i in range(n)]
for _ in range(m):
  a, b, w = [int(i) for i in sys.stdin.readline().split()]
  vizinhos[a-1].append({'vertice':b-1, 'peso':w})
  vizinhos[b-1].append({'vertice':a-1, 'peso':w})

melhor_caminho = dijkstra(vizinhos, n)
for caminho in melhor_caminho:
  caminho = str(caminho)
  print(caminho.replace(',','').replace('[','').replace(']',''))
