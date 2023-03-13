# DICAS SOBRE PYTHON:
# FUNÇÃO, input(): Ela recebe como parâmetro uma String que será visível ao usuário,
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO, print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO split(): permite dividir o conteúdo da variável conforme as condições especificadas
# em cada parâmetro da função ou com os valores predefinidos por padrão;

# Abaixo segue um exemplo de código que você pode ou não utilizar
lados = [float(x) for x in input().split()]

a = lados[0]
b = lados[1]
c = lados[2]

# TODO: Para o cálculo do perímetro triangular aplique seus conhecimentos em Estruturas Condicionais,
# e complete os espaços em branco com as operações que solucionam o desafio.
if a + b > c and b + c > a and c + b > a:
    print(f"Perimetro = {a+b+c:.1f}")
else:
    print(f"Area = { ((a+b)*c) / 2 :.1f}")
