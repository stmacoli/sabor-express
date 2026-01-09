########## Exercicio 1: ##########

escolhido = int(input('Escolha um número: '))

def par_ou_impar(escolhido):
    if escolhido % 2 == 0:
        print('este número é Par')
    else :
        print('este número é Impar')


par_ou_impar(escolhido)


########## Exercicio 2 ##########

idade = int(input('Qual a sua idade: '))

def faicha_etaria(idade):
    if idade >= 0 | idade <= 12 :
        print('Criança')
    elif idade >= 13 | idade <=18 :
        print('Adolescente')
    elif idade >= 19 :
        print('Velho')
    else :
        print('Insira um valor válido')    

faicha_etaria(idade)


########## Exercicio 3 ##########

usuario = input('Insira seu ID: ')
senha = input('Insira sua Senha: ')

def validador(usuario, senha):
    if usuario == 'McLovin' and senha == 'longc':
        print('Seja Bem-vindo Sr. McLovin')
    else :
        print('Usuarios ou Senha inválidos, tente novamente')

validador(usuario, senha)


