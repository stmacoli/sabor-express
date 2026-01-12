import os

restaurantes = ['Si Señor', 'Seu Vidal'] 


def exibir_nome_do_programa():    
    print("""
    🅂 🄰 🄱 🄾 🅁   🄴 🅇 🄿 🅁 🄴 🅂 🅂
            por Steven Barreda
    """)

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes') 
    print('3. Ativar restaurante')
    print('4. Sair \n')

def escolher_opcao():
#   opcao_escolhida = int(input('Escolha uma opção: ')) -> ATENÇÃO: o input recebe sempre STRING por isso em aula
#                                                          usamos o INT para transformar o input em Números Inteiros
#
#
#
#   ######### \/ JEITO CLASSICO DE LAÇO IF \/ ##########
#
#
#    if opcao_escolhida == 1:
#        print('Cadastrar restaurante')
#    elif opcao_escolhida == 2:
#        print('Listar restaurantes')
#    elif opcao_escolhida == 3:
#        print('Ativar restaurante')    
#    else :
#        opcao_invalida()
#
#
# ou com MATCH:
#
#   ######### \/ JEITO MAIS LEGIVEL E MODERNO \/ ##########
#
#    match opcao_escolhida:
#        case 1:
#            print('Cadastrar restaurante')
#        case 2:
#            print('Listar restaurantes')
#        case 3:
#            print('Ativar restaurante')
#        case 4:
#            finalizar_app()
#       case _:
#            print('Não válido')
#        case '1':
#            print('Cadastrar restaurante')
#        case '2':
#            print('Listar restaurantes')
#        case '3':
#            print('Ativar restaurante')
#        case '4':
#            finalizar_app()
#        case _:
#            opcao_invalida()




#
# Para a aula e aprender sobre transformar input em INT vale muito,
# Mas a maneira mais eficiente de se fazer esse menu seria transformar os cases em STRING
# 
# 
# Exemplo: 
#
#     Case 1: -> Case com INT
#         print('Cadastrar restaurante')
#
#       e transformar em:
#
#     Case '1': -> Case com STRING
#         print('Cadastrar restaurante')
#
#
# Pois da maneira que fizemos em aula (transformando o input em INT) e o usuário inserir uma letra ou simbolo, o código quebra.
# INT é usado para fazer matemática, não para controle de fluxo (no caso do menu).

    opcao_escolhida = input('Escolha uma opção: \n')

def opcao_invalida():
    print('Opção Invalída válida \n')
    input('Digite uma tecla para voltar ao menu principal')
    main()


def cadastrar_novo_restaurante():
    os.system('cls')
    print('Cadastro de Novo Restaurante\n')
    nome_do_restaurante = input('Digite o nome do novo restaurante: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O Restaurante {nome_do_restaurante} foi cadastrado com Sucesso!')
    input('Digite uma tecla para voltar ao menu principal.')
    main()

def listar_restaurantes():
    os.system('cls')
    print('Lista de Restaurantes: \n')
    for restaurante in restaurantes:
        print(f'.{restaurante} \n')


    input('Digite uma tecla para voltar ao menu principal \n')
    main()


def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
    

def finalizar_app():
    os.system('cls')
    print('Obrigado por escolher a 🅂 🄰 🄱 🄾 🅁   🄴 🅇 🄿 🅁 🄴 🅂 🅂 ! \n\n\n')
def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)
        
        if opcao_escolhida == 1: 
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2: 
            listar_restaurantes()
        elif opcao_escolhida == 3: 
            print('Ativar restaurante')
        elif opcao_escolhida == 4: 
            finalizar_app()
        else:
            opcao_invalida()
    except: 
        opcao_invalida()



    



if __name__ == '__main__':
    main()
