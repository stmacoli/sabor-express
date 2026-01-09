import os


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
#        finalizar_app()
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

    opcao_escolhida = input('Escolha uma opção: ')



    match opcao_escolhida:
        case '1':
            print('Cadastrar restaurante')
        case '2':
            print('Listar restaurantes')
        case '3':
            print('Ativar restaurante')
        case '4':
            finalizar_app()
        case _:
            print('Não válido')

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

def finalizar_app():
    os.system('cls')
    print('Obrigado por escolher a 🅂 🄰 🄱 🄾 🅁   🄴 🅇 🄿 🅁 🄴 🅂 🅂 ! \n\n\n')

if __name__ == '__main__':
    main()
