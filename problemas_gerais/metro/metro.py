n_s = input().split(' ')
n = int(n_s[0])
s = int(n_s[1])

ida = input().split(' ')
volta = input().split(' ')

# condições
if (ida[0] == '0'):
  print('NO')
elif (ida[s-1] == '1'):
  print('YES')
elif (volta[s-1] == '1'):
  resposta = 'NO'
  for i in range(s,n):
    if (ida[i] == '1' and volta[i] == '1'):
      resposta = 'YES'
  print(resposta)
else:
  print('NO')
