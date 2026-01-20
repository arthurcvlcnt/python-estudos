# # num = 18**(1/2)                                                         descobrindo raiz quadrada
# # print(num)

# # num1 = int(input("digite um número: "))
# # num2 = int(input("digite um número: "))
# # print(f"o resultado é:{num1 * num2}", end= " ! " ) 
# # print(f"{"muito obrigado por usar meu codígo! ":-^20}" )

# # num1 = int(input("digite um número: "))
# # num2 = int(input("digite um número: "))
# # print(f"o resultado é: {num1 * num2}", end=" ! ")
# # print(f"{'muito obrigado por usar meu código!':-^50}")

# num1 = int(input('digite o primeiro numero: '))
# num2 = int(input('digite o segundo numero: '))
# s = num1 + num2
# m = num1 * num2 
# d = num1 / num2 
# di = num1 // num2 
# p =  num1 ** num2
# r = num1 % num2 
# print(f' soma:{s}\n multiplicação:{m}\n divisão:{d:.3f}\n divisão inteira:{di}\n potencia:{p:.3f}\n resto:{r:.3f}') 

#desafio 5 gustavo guanabara!!!!!!!!
 
#----------- exercicio 1 --------------                                  programa que fala o numero sucessor e antecessor

# n1 = int(input('escolha um número'))
# ns = n1 - 1
# na = n1 + 1
# print(f'o numero antecessor de {n1} é o : {n}' )

# ----mais organizado e revisado--

# n = int(input("Escolha um número: "))
# print(f"O número antecessor de {n} é : {n - 1} \nseu sucessor : {n + 1}")

#------------------- exercicio 2 ----------------                         programa que calcula o dobro o triplo e a raiz de um número

# n = int(input('digite um número:'))
# print(f' o dobro de {n} é : {n * 2}\no triplo de {n} é : {n * 3}\n a raiz quadrada de {n} é : {n ** (1/2):.3f}')

#------mais organizado e revisado--

# numero = int(input("Digite um número: "))

# dobro = numero * 2
# triplo = numero * 3
# raiz = numero ** 0.5   # mais direto que (1/2)

# print(f"""
# O número escolhido foi {numero}
#  Dobro: {dobro}
#  Triplo: {triplo}
#  Raiz quadrada: {raiz:.3f}
# """)

#-------- exercicio 3 ---------------                                     programa que le duas notas de um aluno e calcula a media 

# nota1 = float(input('coloque sua primeira nota:'))
# nota2 = float(input('coloque sua segunda nota:'))


# media = (nota1 + nota2 ) / 2

# if media >= 7 :
#      print(f'sua media foi : {media :.3f} aprovado!!! ')
# else:
#     #   print(f'sua media foi : {media :.3f} reprovado!!!')

#----------melhorado----------------------
#não fiz melhorado

#---------------------exercicio 4-----------------------------   programa que converte um número de metros para centimetros e milimetros

# metros = float(input("quantos metros são: "))

# cm = (metros * 100)
# mm = (cm * 1000)    esta errado pois vai converter em mm com o valor do cm para da certo deveria ficar mm = cm * 10 (pois ai ja ia pegar o valor convertido de cm e aproveitar)

# print('---conversões-----')
# print(f'{metros}m = {cm}cm!')
# print(f'{metros}m = {mm}mm!')
#---------------revisado e melhorado-----------------

# Conversor de metros para cm e mm

# metros = float(input("Digite um valor em metros: "))

# cm = metros * 100
# mm = metros * 1000

# print("\n--- Conversões ---")
# print(f"{metros} m = {cm:.0f} cm")
# print(f"{metros} m = {mm:.0f} mm")

#-----------------------------exercicio 5----------------------------- programa que lé um número e mostra a tabuada dele

# num = int(input('escolha um número: '))

# num1 = num * 1
# num2 = num * 2
# num3 = num * 3
# num4 = num * 4
# num5 = num * 5
# num6 = num * 6
# num7 = num * 7
# num8 = num * 8
# num9 = num * 9
# num10 = num * 10

# print(f'a tabuada de {num}: ')
# print(f'{num} * 1 = {num1}')
# print(f'{num} * 2 = {num2}')
# print(f'{num} * 3 = {num3}')
# print(f'{num} * 4 = {num4}')
# print(f'{num} * 5 = {num5}')
# print(f'{num} * 6 = {num6}')
# print(f'{num} * 7 = {num7}')
# print(f'{num} * 8 = {num8}')
# print(f'{num} * 9 = {num9}')
# print(f'{num} * 10 = {num10}')

#-----------------------------------revisado e melhorado---------------------

# Programa que mostra a tabuada de um número

# numero = int(input("Digite um número para ver a tabuada: "))

# print(f"\n--- Tabuada do {numero} ---")
# for i in range(1, 11):
#     print(f"{numero} x {i:2} = {numero * i}")

#--------------- exercicio 6 ------------------------------- programa que le o saldo da sua carteira e converte para dolar (COTAÇÃO DE 3.27)

# carteira = float(input('digite o valor que tem em sua carteira: '))

# dolar = carteira / 3.27 # Divisão para converter reais em dólares

# print(f'com o seu saldo da carteira você consegue comprar {dolar:.2f} dolares!')

#-----------------melhorado e revisado ---------------------


# carteira = float(input("Quanto você tem na carteira (em R$): "))

# cotacao = 3.27
# dolares = carteira / cotacao

# print(f"\nCom R$ {carteira:.2f} você pode comprar US$ {dolares:.2f} (cotação: {cotacao})")

#---------------exercicio 7 --------------------------  programa que calcula a area da parede e fala quantos litros de tinta deve utilizar(tendo em vista que 1 = 2m2)

# altura = float(input('digite a altura da parede: '))
# largura = float(input('digite a largura da parede: '))

# area = altura * largura
# rendimento = 2

# tinta_necessaria = area / rendimento 

# print(f"a quantidade de tinta necessaria para pintar a parede é de {tinta_necessaria}litros")

#----------------revisado e melhorado----------------------

# # Entrada de dados: altura e largura da parede
# altura = float(input("Digite a altura da parede (em metros): "))
# largura = float(input("Digite a largura da parede (em metros): "))

# # Cálculo da área da parede
# area = altura * largura

# # Rendimento da tinta (quantos m² cada litro cobre)
# rendimento = 2  # 1 litro de tinta cobre 2 m²

# # Cálculo da quantidade de tinta necessária
# tinta_necessaria = area / rendimento

# # Exibição dos resultados
# print("\n--- Resultado ---")
# print(f"A área da parede é de {area:.2f} m².")
# print(f"Você precisará de {tinta_necessaria:.2f} litros de tinta para pintá-la.")

#----------------exercicio 8-------------------------------- programa que le o preço do produto e mostra com 5% de desconto

# preço = float(input('digite o preço do produto: '))

# desconto = preço * 0.05
# preço_com_desconto = preço - desconto

# print(f'o preço do produto é de {preço}')
# print(f'com o desconto de {desconto}, o valor do produto fica {preço_com_desconto}')

#-----------codigo melhorado e revisado---------------

# Programa que calcula 5% de desconto em um produto

# preco = float(input("Digite o preço do produto (R$): "))

# desconto = preco * 0.05   # 5% do preço
# preco_final = preco - desconto

# print(f"\nPreço original: R$ {preco:.2f}")
# print(f"Desconto (5%):  R$ {desconto:.2f}")
# # print(f"Preço com desconto: R$ {preco_final:.2f}")

#--------------------exercicio 9 -------------------------------- programa que le o salario atual da pessoa e calcula com aumento(15%)

# salario = float(input('digite o valor do seu salario atual: '))

# aumento = (salario * 0.15) + salario

# print(f'seu salario atual é de {salario}')
# print(f'com o aumento de 15%. o seu salario é de {aumento}')

#---------- revisado e melhorado ------------

# Programa que calcula aumento de 15% no salário

# salario = float(input("Digite o salário atual (R$): "))

# aumento = salario * 0.15    # 15% do salário
# novo_salario = salario + aumento

# print(f"\nSalário atual: R$ {salario:.2f}")
# print(f"Aumento (15%): R$ {aumento:.2f}")
# print(f"Novo salário:  R$ {novo_salario:.2f}")

#----------exercicio 10 ------------------ conversor de temperatura de °c para °f (9 * °c / 5 + 32)

# c = float(input('qual temperatura em graus C° : '))

# print(f'a temperatura {c}c° em  Fahrenheit é {((9*c)/5)+32}°f')

#--------- revisado e melhorado------------

#n tem

#-------------excercicio 11 ---------------- aluguel de carros

# dias = int(input('quantos dias você ficou com o carro : '))
# km = float(input('quantos km você andou com o carro: '))

# print(f'pelos dias que você usou que foram {dias}, você deve pagar {dias * 60}\n e pelos km que você andou com o carro que foi {km} você deve pagar {km * 0.15}')
# # print(f'somando tudo você deve pagar {(dias*60)+(km*0.15)}')

#---------------------------------------------------------------------------------------------------------------------------------------------
