#----Computação Monetária----#
#Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. 
# A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. 
# As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias. 
# Entrada
# O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).
# Saída
# Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.
# Obs: Utilize ponto (.) para separar a parte decimal.

valor_Monetario =float(input())
centavos = int(round(valor_Monetario * 100))
notas = [100, 50, 20, 10, 5, 2]
moedas = [100, 50, 25, 10, 5, 1] # 1 real = 100 cenavos, para evitar erros em atribuição de contas
#PROCESSAMENTO DE NOTAS:
print("NOTAS:")
for nota in notas:
    qtd_notas = centavos // (nota * 100)
    print(f"{qtd_notas} nota(s) de R$ {nota}.00")
    centavos %= (nota * 100)
 #PROCESSAMENTO DAS MOEDAS
print("MOEDAS:")
print(f"{centavos // 100} moeda(s) de R$ 1.00")
centavos %= 100
for moeda in moedas[1:]:  # Pula a moeda de 1 real, já feito antes!!
    qtd_moedas = centavos // moeda
    print(f"{qtd_moedas} moeda(s) de R$ {moeda / 100:.2f}")
    centavos %= moeda 
