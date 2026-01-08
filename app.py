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
    opcao_escolhida = int(input('Escolha uma opção: '))

#JEITO CLASSICO DE LAÇO IF
#    if opcao_escolhida == 1:
#        print('Cadastrar restaurante')
#    elif opcao_escolhida == 2:
#        print('Listar restaurantes')
#    elif opcao_escolhida == 3:
#        print('Ativar restaurante')    
#    else :
#        finalizar_app()

# \/ JEITO MAIS LEGIVEL E MODERNO \/

    match opcao_escolhida:
        case 1:
            print('Cadastrar restaurante')
        case 2:
            print('Listar restaurantes')
        case 3:
            print('Ativar restaurantee')
        case 4:
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
