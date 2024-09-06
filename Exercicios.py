# 1 - Crie uma lista para cada informação a seguir:
# Lista de números de 1 a 10;
numeros_1_a_10 = list(range(1, 11))

# Lista com quatro nomes;
nomes = ["Luiz", "Luiza", "Mateus", "Gabrielle"]

# Lista com o ano que você nasceu e o ano atual.
ano_nascimento = 2007
ano_atual = 2024
anos = [ano_nascimento, ano_atual]

# Mostre na tela o conteudo das listas.
print(f"Lista de números de 1 a 10: {numeros_1_a_10}")
print(f"Lista com quatro nomes: {nomes}")
print(f"Lista com o ano de nascimento e o ano atual: {anos}")

# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
lista_exemplo = [1, 2, 3, 4, 5]
print("Percorrendo a lista exemplo:")
for elemento in lista_exemplo:
    print(elemento)

# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
soma_impares = 0
for numero in range(1, 11):
    if numero % 2 != 0:
        soma_impares += numero
print(f"Soma dos números ímpares de 1 a 10: {soma_impares}")

# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
print("Números de 1 a 10 em ordem decrescente:")
for numero in range(10, 0, -1):
    print(numero)

# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
numero_usuario = int(input("Digite um número para ver a tabuada: "))
print(f"Tabuada de {numero_usuario}:")
for i in range(1, 11):
    print(f"{numero_usuario} x {i} = {numero_usuario * i}")

# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.
lista_numeros = [5, 10, 15, 20]
soma_total = 0
try:
    for numero in lista_numeros:
        soma_total += numero
except Exception as e:
    print(f"Erro ao calcular a soma: {e}")
else:
    print(f"Soma de todos os elementos da lista: {soma_total}")

# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.
def calcular_media(lista):
    try:
        media = sum(lista) / len(lista)
    except ZeroDivisionError:
        print("A lista está vazia. Não é possível calcular a média.")
        return None
    return media

lista_valores = list(map(int,input('Digite os números para compor a lista separados por espaço: ').split())) 
media_valores = calcular_media(lista_valores)
if media_valores is not None:
    print(f"Média dos valores na lista: {media_valores}")