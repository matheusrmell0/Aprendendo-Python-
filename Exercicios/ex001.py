from math import sqrt, ceil, floor, pow, sqrt, tan, cos, sin, radians
from datetime import date
import datetime
from random import randint, choice, shuffle

n1 = int(input('Digite um número'))
n2 = int(input('Digite outro número'))
result = (n1 + n2)
print('O resultado de {} + {} é igual a {}'.format(n1,n2,result))

value = input('Digite um valor')
isnum = value.isnumeric()
isalpha = value.isalpha()
isalnum = value.isalnum()
type = type(value)
space = value.isspace()
uperCase = value.isupper()
lowerCase = value.islower()
capitalize = value.istitle()

print('O valor é do tipo: {}'.format(type))
print('O valor é um alpha númerico?: {}.'.format(isalpha))
print('O valor é uma string?: {}'.format(isalpha))
('O valor é um número?: {}'.format(isnum))
print('O valor tem espaços?: {}'.format(space))
print('O valor só tem letras maiusculas?: {}'.format(uperCase))
print('O valor só tem letras minusculas?: {}'.format(lowerCase))
print('O valor só tem letras minusculas?: {}'.format(lowerCase))
print('O valor esta capitalize?: {}'.format(capitalize))

nome = str(input('Qual seu nome?'))
('Prazer te conhecer {:0^20}!'.format(nome))

n1 = int(input('Digite um valor'))
n2 = int(input('Digite outro valor'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, \n o produto é {}, \n a divisão é {:.3f}'.format(s,m,d), end=' ')
print('A divisão inteira é {}, e a potencia é {}'.format(di,e))

number = int(input('Digite um número inteiro'))
print('O número é {} \n seu antecessor é {} \n seu sucessor é {}'.format(number, number - 1, number + 1))

value = int(input('Digite um número'))
print('O número é {} \n  Seu dobro é {} \n  Seu triplo é {} \n  Sua raiz quadrada é {}'.format(value, value * 2, value * 3, value ** (1/2)))
55

nota1 = int(input('Nota do primeiro aluno'))
nota2 = int(input('Nota do segundo aluno'))
list = [nota1, nota2]
print('A nota do primeiro aluno é {}, e5 a do segundo é {} \n A média dos dois foram {}'.format(list[0], list[1], (list[0] + list[1] )/ len(
    list)))

meters = int(input('O valor em metros'))
print('O valor em metros é: {}m, O valor em centímetros {:.0f}cm, O valor em milímetros: {:.0f}mm'.format(meters, meters * 100, meters * 1000))


num = int(input('Um número para mostrar sua tabuada'))
print('A tabuada de {} é: \n de 1 = {}, de 2 = {}, de 3 = {}, de 4 = {}, de 5 = {}, de 6 = {}, de 7 = {}, de 8 = {}, de 9 = {}, de 10 = {}'.format(num, num * 1, num * 2, num * 3, num * 4, num * 5, num * 6, num * 7, num * 8, num * 9, num * 10))

real = float(input('Valor em R$'))
print('O valor de {}R$ é igual a {:.2f}$ em 2018'.format(real, real / 3.27))
print('Com {} reais, você compra {:.2f} unidades de dolares'.format(real, real // 3.27))

alt = float(input('Altura em metros'))
larg = float(input('Largura em metros'))
area = (alt * larg)
print('Uma parede de {}m de altura e {}m de largura tem uma área de {}m², para pintar toda esse comodo com uma tinta que preenche 2m² por litro será necessária {}L de tinta'.format(alt, larg, area, area / 2))

produto = float(input('Valor do produto'))
print('O produto tem um valor de {}R$, mas com 5% de desconto ele fica por {:.2f}R$'.format(produto, produto - (produto * 0.05)))

salario = float(input('Salario do funcionario é:'))
porcent = float(input('Aumento em %'))
print('O salario do funcionario que era de {}R$ teve um aumento de {}% e agora é {:.2f}R$!!'.format(salario, porcent, salario + (salario * (porcent / 100))))

km = float(input('Quantos Km você percorreu com o carro?'))
days = int(input('Quantos dias esse carro foi alugado?'))
price = days * 60 + (km * 0.15)
print('O preço a pagar será de: R${:.2f}'.format(price))

num = int(input(('Digite um número')))
raiz = sqrt(num)
print('O número é {}, e sua raiz quadrada é {}'.format(num, ceil(raiz)))

num = float(input('Digite um número'))
numInt = floor(num)
print('O valor inteiro do número {}  {}'.format(num, numInt))

catOposto = float(input('Digite o valor do cateto oposto'))
catAdjacente = float(input('Digite o valor do cateto adjacente'))
print('O comprimento da hipotenusa é {}'.format(sqrt((pow(catOposto,2) + pow(catAdjacente,2)))))

an = float(input('Digite um ângulo'))
sen = sin(radians(an))
cos = cos(radians(an))
tan = tan(radians(an))
print('O ângulo de {} tem o seno de {:.2f}, cosseno de {:.2f} e tangente de {:.3f}'.format(an, sen, cos, tan))

randomNum = randint(0,3)
list = ['Maria', 'João', 'Pedro', 'Lucas']
print('O aluno sorteado para apagar o quadro será {}'.format(list[randomNum]))
print('O aluno sorteado para apagar o quadro será {}'.format(choice(list)))

n1 = str(input('Digite o primeiro nome'))
n2 = str(input('Digite o segundo nome'))
n3 = str(input('Digite o terceiro nome'))
n4 = str(input('Digite o quarto nome'))
nomes = [n1, n2, n3, n4]
shuffle(nomes)
print('A lista de nomes é')
print(nomes)


phrase = str(input('Digite uma frase')).upper()
print(phrase.strip().count('A'))
print(phrase.strip().find('A'))
print(phrase.strip().rfind('A'))

name = str(input('Digite seu nome completo'))
print(name.upper())
print(name.lower())
print(name.strip().replace(' ',''))
print(len(name.split()[0]))

num = str(input('Digite um número de 0 a 9999'))[0:4]
print('Unidade: {} \n Dezena: {} \n Centena: {} \n Milhar: {}'.format(num[3], num[2], num[1], num[0]))

city = str(input('Digite sua cidade'))
print('santo' in city.lower().strip().split()[0])

nome = str(input('Digite o nome'))
print('silva' in nome.lower().strip())

nomeInteiro = str(input('Digite o nome inteiro'))
print('Nome: {} \n Primeiro nome: {} \n Ultimo nome: {}'.format(nomeInteiro, nomeInteiro.strip().split()[0], nomeInteiro.strip().split()[len(nome) - 1]))

nome = str(input( 'Digite seu nome'))
if nome == 'Matheus':
    print('Que lindo nome {}!'.format(nome.capitalize()))
    print('Bom dia, {}!'.format(nome.capitalize()))
    print('Que loucura você {}'.format(nome))
else:
    print('Teu nome {} não ta nos dados rapa!'.format(nome))


num = randint(0,5)

print('Descruba o número de 0 a 5')
yourNum = int(input('Digite o número'))

if num == yourNum:
    print('Seu número {} é igual ao do computador {}!!!'.format(yourNum, num))
elif yourNum > 5 and yourNum < 0:
   print('Seu número {} não pode ser maior que 5'.format(yourNum))
else:
    print('Seu número {} não é o mesmo do computador {}'.format(yourNum, num))

vel = float(input('Qual a velocidade do seu carro?'))
if vel > 80.0:
    print('Você foi multado!!')
    print('A multa é R$7,00 por Km acima do limite, portanto sua multa será de R${:.2f}'.format((vel - 80) * 7).replace('.',','))

num = int(input('Digite um número'))
if num & 2 == 0:
    print('O número {} é par'.format(num))
else:
    print('O número {} é ímpar'.format(num))

distance = float(input('Qual a distancia da sua viagem em Km?'))
if distance <= 200:
    print('A passagem será de R${:.2f}'.format(distance * 0.5).replace('.',','))
else:
    print('A passagem será de R${:.2f}'.format(distance * 0.45).replace('.',','))

ano = int(input('Digite o ano'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Ano bissexto!!')
else:
    print('Não é ano bissexto')

sal = float(input('Qual o salario'))
if sal > 1250.00:
    print('O salario com aumento de 10% vai ser de {}'.format(sal + (sal * 0.1)))
else:
    print('O salario com aumento de 15% vai ser de {}'.format(sal + (sal * 0.15)))

text = str(input('Escreve seu textinho papai'))
print('{}{}{}'.format('\033[7;33;40m', text ,'\033[m'))

text = str(input('Textinho dois escreva papai'))
print('{}{}{}'.format('\033[4;32;46m', text, '\033[m'))

colors = {
    'green/blue': '\033[4;32;46m',
    'red/yellow': '\033[4;31;43m',
    'pink/white': '\033[4;35;40m'
}

text = str(input('Textinho dois escreva papai'))
print('{}{}{}'.format(colors['green/blue'], text, '\033[m'))
print('{}{}{}'.format(colors['red/yellow'], text , '\033[m'))
print('{}{}{}'.format(colors['pink/white'], text, '\033[m'))

obj = {
    'print' : print('{}{}{}'.format(colors['green/blue'], 'Ola mundo', '\033[m')),
    'print2' : print('{}{}{}'.format(colors['green/blue'], text, '\033[m'))
    }

print(obj['print'])
print(obj['print2'])

print('='*20)
valor = float(input('Qual o valor do \033[4;35;40m imovél \033[m?'))
sal = float(input('Qual a renda \033[4;33;40m mensal \033[m?'))
years = int(input('Quantas prestações em \033[4;34;40m anos? \033[m'))
print('='*20)

if valor / (years * 12) > sal * 0.3:
    print('\033[4;31;40m {} \033[m'.format('Empréstimo negado!'))
else:
    print('\033[7;33;40m {} \033[m'.format('Empréstimo aprovado!'))
    print('Seu valor de \033[3;32;40m R${} \033[m corresponde a menos de 30% de sua renda mensal, logo seu empréstimo foi deferido!'.format(sal))

print('='*50)
n1 = int(input('Escreva um número inteiro'))
print('\033[7;33;40m [1] Para converter em binário \033[m')
print('\033[7;33;40m [2] Para converter em octal \033[m')
print('\033[7;33;40m [3] Para converter em hexadecimal \033[m')
number = int(input('Digite a escolha'))
print('='*50)

if number == 1:
    print('\033[3;32;40m o valor do número \033[m \033[3;33;40m {} \033[m em binário é \033[3;32;41m {} \033[m'.format(n1, bin(n1)))
elif number == 2:
    print('\033[3;32;40m o valor do número \033[m \033[3;33;40m {} \033[m em binário é \033[3;32;41m {} \033[m'.format(n1,oct(n1)))
elif number == 3:
    print('\033[3;32;40m o valor do número \033[m \033[3;33;40m {} \033[m em binário é \033[3;32;41m {} \033[m'.format(n1,hex(n1)))
else:
    print('\033[3;31;40m Digite uma das escolhas acima \033[m')

n1 = int(input('Digite um número'))
n2 = int(input('Digite outro número'))

if n1 > n2:
    print('O valor de {} é maior que o valor de {}'.format(n1, n2))
elif n1 < n2:
    print('O valor de {} é maior que o valor de {}'.format(n2, n1))
else:
    print('O valor de {} é igual ao valor de {}'.format(n1,n2))

ano = str(input('Digite o ano de seu nascimento!'))
mes = str(input('Digite o mês de seu nascimento!'))
dia = str(input('Digite o dia de seu nascimento!'))

niver = {
    'ano': ano,
    'mes': mes.replace('0',''),
    'dia': dia,
    'data': [('{}/{}/{}'.format(dia,mes,ano)), 'Não é uma data válida!']
}

print('\033[3;33;40m==\033[m' * 20)
if len(niver['ano']) > 3 and len(niver['dia']) > 1 and len(niver['mes']) > 1:
    print('\033[4;32;40mSeu aniversário é na data de {} \033[m'.format(niver['data'][0]))
else:
    print('\033[4;32;40m {} \033[m'.format(niver['data'][1]))

UNIX_EPOCH = datetime.datetime(int(niver['ano']), int(niver['mes']), int(niver['dia']))
actual = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day)
difference = ((((actual - UNIX_EPOCH).total_seconds()) / 3600) / 24).__ceil__()

if difference < 6574:
    print('\033[3;31;40mJá se passou o tempo do tempo de alistamento!\033[m')
    print('\033[7;31;40mPassaram-se {} dias do prazo de alistamento\033[m'.format(6574 - difference))
elif difference > 6574:
    print('\033[3;32;40mVocê não precisa se alistar no serviço militar ainda.\033[m')
else:
    print('\033[3;33;40mVocê precisa se alistar no serviço militar!\033[m')
print('\033[3;33;40m==\033[m' * 20)

idade = int(input('Idade do atleta'))

atletasClasse = {
    'mirim': {
        'idade': 9,
        'categoria': 'Mirim'
    },
    'infantil': {
        'idade': 14,
        'categoria': 'Infantil'
    },
    'junior': {
        'idade': 19,
        'categoria': 'Junior'
    },
    'senior': {
        'idade': 20,
        'categoria': 'Sênior'
    },
    'master': {
        'categoria': 'Master'
    }
}

if idade <= atletasClasse['mirim']['idade']:
    print('Categoria \033[3;32;40m{}\033[m'.format(atletasClasse['mirim']['categoria']))
elif idade <= atletasClasse['infantil']['idade']:
    print('Categoria \033[3;32;40m{}\033[m'.format(atletasClasse['infantil']['categoria']))
elif idade <= atletasClasse['junior']['idade']:
    print('Categoria \033[3;32;40m{}\033[m'.format(atletasClasse['junior']['categoria']))
elif idade <= atletasClasse['senior']['idade']:
    print('Categoria \033[3;32;40m{}\033[m'.format(atletasClasse['senior']['categoria']))
else:
    print('Categoria \033[3;32;40m{}\033[m'.format(atletasClasse['master']['categoria']))

preco = float(input('Valor do produto'))

condicao = {
    '1': preco - (preco * .1),
    '2': preco - (preco * .05),
    '3': preco * 1,
    '4': preco + (preco * .2)
}

print('-'*30)
print('Escolha o tipo de pagamento')
print('[1] À vista no dinheiro')
print('[2] À vista no cartão')
print('[3] 2x no cartão')
print('[4] 3x no cartão')
print('-'*30)

type = str(input('Tipo de pagamento'))
if condicao[type]:
    print('O valor a ser pago será de R${:.2f}'.format(condicao[type]))
else:
    print('O tipo de pagamento não foi encontrado')

jokenpo = {
    1: 'Pedra',
    2: 'Papel',
    3: 'Tesoura'
}

print('-'*20)
print('Jokenpô!')
print('[1] Pedra')
print('[2] Papel')
print('[3] Tesoura')
play = int(input('Escolha sua jogada'))
print('-'*20)

math = {
    'computer': randint(1,3),
    'player': play
}

print('Sua jogada foi: {}'.format(jokenpo[math['player']]))
print('A jogada do computador foi: {}'.format(jokenpo[math['computer']]))

mathVar = {
    'computer': jokenpo[math['player']],
    'player': jokenpo[math['computer']]
}

if mathVar['computer'] == mathVar['player']:
    print('Empate!')
elif mathVar['computer'] == 'Tesoura' and mathVar['player'] == 'Papel' or mathVar['computer'] == 'Pedra' and mathVar['player'] == 'Tesoura' or mathVar['computer'] == 'Papel' and mathVar['player'] == 'Pedra':
    print('Vitoria jogador!')
else:
    print('Vitoria computador!')