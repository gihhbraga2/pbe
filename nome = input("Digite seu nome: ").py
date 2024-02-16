nome = input("Digite seu nome: ")

idade = input("Digite sua idade: ")

print('Olá', nome, 'você tem',idade, 'anos')

#lista de exercícios
#1) crie um programa que peça 3 notas e some as trẽs,
#depois mostre o valor

nota1 = float(input("informe a nota 1:"))
nota2 = float(input("informe a nota 2:"))
nota3 = float(input("informe a nota 3:"))

somaNotas= nota1+nota2+nota3

#2) crie um programa que some 4 numeros e calcule a média,
#depois mostre o valor

num1 =float(input("informe o primeiro valor: "))
num2 =float(input("informe o segundo valor: "))
num3 =float(input("informe o terceiro valor: "))
num4 =float(input("informe o quarto valor: "))

media = ((num1 + num2 + num3 + num4)   / 4)

print(' a media eh: ', media)

#3) crie um programa que informe o ano de nascimento
#e calcule a idade

anoNasc= float (input ("informe o ano de nascimento"))
idade = 2024 - anoNasc

print("a idade eh:  ", idade)