
x = int(input())
n = list()

#TODO: Complete os espaços em branco com uma solução possível para o problema.

for i in range(0, 10):
  n.append(x)
  x = n[i]*2
  print(f"N[{i}] = {n[i]}")
