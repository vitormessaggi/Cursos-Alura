import os

resturantes = ['pizza','hamburguer']

def exibir_nome():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░\n""")

def escolher_opcao():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair\n')

def finalizar_app():
    mostrar_subtitulo('Finalizando Programa... zx')

def menu():
    input('Precione uma tecla para retomar ao menu \n')
    main()

def mostrar_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def opcao_invalida():
    os.sustem('cls')
    print('Digite uma opção válida!')
    menu()

def cadastrar_restaurante():
    mostrar_subtitulo('Cadastro de novos restaurantes')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    resturantes.append(nome_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso! ')
    menu()  

def listar_restaurantes():
    mostrar_subtitulo('Restaurantes cadastrados!')

    for restaurante in resturantes:
        print(f'->{restaurante}')
    
    menu()

def exibir_opcao():
    try:
        opcao = int(input('Escolha uma opção: '))
        print(f'Você escolheu: {opcao}')


        if opcao == 1:
            cadastrar_restaurante()

        elif opcao == 2:
            listar_restaurantes()

        elif opcao == 3:
            print('Ativar restaurantes')
        
        elif opcao == 4:
            finalizar_app()

        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome()
    escolher_opcao()
    exibir_opcao()


if __name__ == '__main__':
    main()