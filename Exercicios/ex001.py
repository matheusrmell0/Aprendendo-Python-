from math import sqrt, ceil, floor, pow, sqrt, tan, cos, sin, radians
from num2words import num2words
from datetime import date
import datetime
import requests
from time import sleep
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

randomNum = randint(0, 3)
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
print(name.strip().replace(' ', ''))
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

for i in range(10, 0, -1):
    sleep(1)
    print(i)
sleep(1)
print('Bum!!')

for i in range(1 , 50):
    if i % 2 == 0:
        print(i)

for i in range(1, 500):
    if i % 2 != 0 and i % 3 == 0:
        print(i)

num = int(input('Escreva um número:'))
print('A tabuada de {} é:'.format(num))
print('=-' * 11)
for i in range(0, 11):
    print('Tabuada de {} para {} é: {}'.format(num, i, num * i))
print('=-'*11)

value = 0
for i in range(0, 7):
    numb = int(input('Digite um número:'))
    if numb % 2 == 0:
        value += numb
print('A soma dos números pares digitados foi {}'.format(value))

termo = int(input('Digite o valor do termo da PA'))
razao = int(input('Digite o valor da razão da PA'))

for i in range(0, termo, razao):
    print(i)

number = int(input('Numero: '))
if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print(number, 'não é primo')
            break
    else:
        print(number, 'é primo')
elif number == 0:
    print(number, 'é zero')
elif number == 1:
    print(number, 'é um')
else:
    print(number, 'é negativo')

scr = str(input('Digite a frase ou palavra')).strip().lower().replace(' ', '')

word = []
word2 = []

for i in range(len(scr), 0, -1):
    word.append(scr[i - 1])

for c in range(0, len(scr)):
    word2.append(scr[c])

if word == word2:
    print('A frase ou palavra é um políndromo!!')
else:
    print('A frase ou palavra não é considerado um políndromo!')

years = []
for y in range(0, 7):
    year = int(input('Digite o ano de nascimento'))
    years.append(year)

for x in range(0, len(years)):
    if date.today().year - years[x] >= 21:
        print('As pessoas que nasceram em {}, já são maiores de idade!'.format(years[x]))
    else:
        print('As pessoas que nasceram em {}, não são maiores de idade!'.format(years[x]))

maior = 0
menor = 0
for i in range(1, 6):
    peso = float(input('Digite o peso da pessoa número {}: '.format(i)))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < maior:
            menor = peso
print('O menor peso lido foi de {}Kg'.format(menor))
print('O maior peso lido foi de {}Kg'.format(maior))

pessoasList = []
for i in range(0, 4):
    print('----', i + 1, 'Pessoa ----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ')).strip().upper()
    pessoas = {
        'pessoa{}'.format(i): [
            nome,
            idade,
            sexo,
        ]
    }
    pessoasList.append(pessoas)

media = 0
woman = []
oldMan = []
olderAge = 0

for p in range(0, len(pessoasList)):
    media += pessoasList[p]['pessoa{}'.format(p)][1] / len(pessoasList)
    if pessoasList[p]['pessoa{}'.format(p)][2] == 'F' and pessoasList[p]['pessoa{}'.format(p)][1] < 20:
        woman.append(pessoasList[p]['pessoa{}'.format(p)][2])
    if p == 0 and pessoasList[p]['pessoa{}'.format(p)][2] in 'M':
        olderAge = pessoasList[p]['pessoa{}'.format(p)][1]
    if pessoasList[p]['pessoa{}'.format(p)][2] in 'M' and pessoasList[p]['pessoa{}'.format(p)][1] > olderAge:
        oldMan.append(pessoasList[p]['pessoa{}'.format(p)])

print('A média de idade do grupo é de {} anos'.format(media))
if len(oldMan) > 0:
    print('O homem mais velho tem {:.0f} anos e se chama {}'.format(oldMan[0][1], oldMan[0][0]))
else:
    print('Não existem homens nessa lista')
if len(woman) > 0:
    print('Ao todo são {} mulheres com menos de 20 anos'.format(woman.count('F')))
else:
    print('Não existem mulheres com menos de 20 anos na lista')

var = ['M', 'F']
sexo = ''
while not('M' in sexo or 'F' in sexo):
    sexo = str(input('Digite seu sexo'))
    if sexo == var[0]:
        print('Masculino')
    elif sexo == var[1]:
        print('Feminino')

computer = -2
player = -1
tentativas = 1
print('-=' * 22)
print('Adivinhe o número do computador entre 0 e 10!')
while not(computer == player):
    computer = randint(0,10)
    player = int(input('Digite um número entre 0 e 10 '))
    print(computer)
    print(player)
    if computer == player:
        print('Você acertou o número!')
        print('Você tentou {} vezes antes de acertar!'.format(tentativas))
    else:
         print('Errado tente novamente...')
         tentativas += 1

num = float(input('Digite um número'))
num2 = float(input('Digite o segundo número'))
exit = 0

print('-=' * 10)
print('Digite [1] para Somar')
print('Digite [2] para Multiplicar')
print('Digite [3] para saber o Maior')
print('Digite [4] para digitar novos valores')
print('Digite [5] para sair do programa')
while exit != 5:
    exit = int(input('Digite o comando'))
    print('-=' * 10)
    if exit == 1:
        print('A soma dos dois valores é de {:.1f}'.format(num + num2))
    elif exit == 2:
        print('A multiplicação dos dois valores é de {:.1f}'.format(num * num2))
    elif exit == 3:
        if num > num2:
            maior = num
        else:
            maior = num2
        print('O maior valor é o {:.1f}'.format(maior))
    elif exit == 4:
        num = float(input('Digite novamente um número'))
        num2 = float(input('Digite novamente o segundo número'))
    else:

        print('Programa finalizado')

valor = int(input('Digite um número para saber seu fatorial'))
result = valor
fatorial = []
i = 0
while i != 1:
    for i in range(valor - 1,0,-1):
        fatorial.append(i)
for i in range(len(fatorial),0, -1):
    result *= i
finalResult = ('{}! = {} = {}'.format(valor,fatorial,result))
print(finalResult.replace(',',' x'))

soma = 0
cont = 0
while True:
    num = int(input('Digite um valor '))
    if num == 999:
        break
    soma += num
    cont += 1

print(f'A soma dos {cont} números digitados'
      f' foi de {soma}')

tab = 1
while tab:
    tab = int(input('Digite um valor: '))
    if tab < 0:
        break
    print('-=' * 15)
    print(f'Tabuada de {tab}:')
    for i in range(0, 11):
        print(f'{tab} x {i} = {tab * i}')
    print('-=' * 15)
print('Tabuada finalizada!')

while True:
    print('-=' * 22)
    player = int(input('Digite um valor: '))
    play = str(input('Digite par ou ímpar [P/I]: ')).upper()
    print('-=' * 22)
    cpu = randint(0, 999)
    result = cpu + player
    if play == 'I':
        print(f'O computador jogou {cpu} e você {player} escolhendo Ímpar')
        if result % 2 != 0:
            print('-' * 45)
            print(f'Resultado {result} Ímpar!! Você venceu!')
            print('-' * 45)
        else:
            print('-' * 45)
            print(f'Resultado {result} Par!! Você perdeu!')
            print('Fim do jogo')
            print('-' * 45)
            break
    else:
        print(f'O computador jogou {cpu} e você {player} escolhendo Par')
        if result % 2 == 0:
            print('-' * 45)
            print(f'Resultado {result} Par!! Você venceu!')
            print('-' * 45)
        else:
            print('-' * 45)
            print(f'Resultado {result} Ímpar!! Você perdeu!')
            print('Fim do jogo')
            print('-' * 45)
            break

pessoas = 0
sexos = []

while True:
    print('Cadastrar usuário')
    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input('Digite o sexo da pessoa [M/F]: ')).upper().strip()
    if idade > 18:
        pessoas += 1
    if sexo == 'M':
        sexos.append(sexo)
    elif idade < 20 and sexo == 'F':
        sexos.append(sexo)
    if idade > 0 and len(sexo) > 0:
        cadastro = str(input('Gostaria de cadastrar outro usuário? [S/N]')).upper().strip()
        if cadastro == 'N':
            break

print('Foram castradas {} pessoas com mais de 18 anos'.format(pessoas))
print('Foram cadastrados {} homens'.format(sexos.count('M')))
print('Foram cadastradas {} mulheres com menos de 20 anos'.format(sexos.count('F')))

produtos = {
    'preço': [],
    'nome': [],
    'total': 0,
    'maior1000': 0,
}

while True:
    print('Cadastrar produto:')
    nome = str(input('Nome do produto: ')).lower().strip().capitalize()
    value = float(input('Preço do produto: '))

    produtos['nome'].append(nome)
    produtos['preço'].append(value)
    produtos['total'] += value

    if value > 1000:
        produtos['maior1000'] += 1

    clear = str(input('Gostaria de cadastrar outro produto? [S/N]')).upper().strip()
    if clear == 'N':
        break

minorPrice = min(produtos['preço'])
print('*=' * 40)
print('O total gasto na compra foi de {:.2f}'.format(produtos['total']))
print('Temos {} produtos que custam mais que R$1000'.format(produtos['maior1000']))
index = produtos['preço'].index(min((produtos['preço']) for produtos['preço'] in produtos['preço']))
print('O produto mais barato é o {} e custa R${:.2f}'.format(produtos['nome'][index], minorPrice))
print('=*' * 40)

print('*=' * 40)
print('ATM')
print('=*' * 40)

value = int(input('Digite o valor que quer sacar'))
total = value
cedula = 50
totalCedulas = 0

while True:
    if total >= cedula:
        total -= cedula
        totalCedulas += 1
    else:
        if totalCedulas > 0:
            print('Total de {} cédulas de R${}'.format(totalCedulas, cedula))
        elif cedula == 50:
            cedula = 10
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalCedulas = 0
        if total == 0:
            break

tupla = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)

num = int(input('Digite um número'))

while True:
    if tupla.count(num) != 0:
        print('Você digitou o número {}'.format(num2words(num, lang='pt-br')))
        break
    else:
        num = int(input('Digite um número entre 0 e 20'))

auth_token = 'live_e5748c7d449b5b48d6055cd803efe4'
headers = {'Authorization': f'Bearer {auth_token}'}
url = 'https://api.api-futebol.com.br/v1/campeonatos/10/fases/317'
response = requests.get(url, headers=headers)

times = []
def funcaoBra23(time):
    return times.append(time)

print('*=' * 12)
print('Tabela Brasileirão 2023')
print('*=' * 12)

for i in range(0, len(response.json()['tabela'])):
    print('{}º Lugar: {}'.format(i + 1, response.json()['tabela'][i]['time']['nome_popular']))
    funcaoBra23(response.json()['tabela'][i]['time']['nome_popular'])

print('Os 5 primeiros colocados são {}'.format(times[0:5]).replace('[', '').replace(']', '').replace("'", ''))

for i in range(0, len(times[::-1][0:4])):
    print('Os 4 últimos colocados são os times: {}'.format(times[::-1][0:4]).replace('[', '').replace(']', '').replace("'", ''))

produtos = ('Lápis', 1.75, 'Borracha', 2.0, 'Caderno', 15.9, 'Estojo', 25.0, 'Mochila', 120.32)
preco = []
nome = []

for i in range(0, len(produtos)):
    if type(produtos[i]) == str:
        nome.append(produtos[i])
    else:
        preco.append(produtos[i])

if len(preco) > 0 and len(nome) > 0:
    for i in range(0, len(produtos)):
        print('{}.....{}'.format(nome[i], preco[i]))
