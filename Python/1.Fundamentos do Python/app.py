import os

restaurantes = [{'nome':'Cantina', 'categoria':'Italiana', 'ativo': 'False'},
               {'nome':'Sabores', 'categoria':'Brasileira', 'ativo':'True'}]

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
    print('3. Alterar estado do Restaurante')
    print('4. Sair\n')

def finalizar_app():
    mostrar_subtitulo('Finalizando Programa... zx')

def menu():
    input('Precione uma tecla para retomar ao menu \n')
    main()

def mostrar_subtitulo(texto):
    os.system('cls')
    line = '-' * len(texto)
    print(line)
    print(texto)
    print(line)
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

    print(f'{'Nome do restaurante'.ljust(23)} | {'Categoria'.ljust(20)} | {'Situação de funcionamento'}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        situacao = 'ativo' if restaurante['ativo'] else 'desativado'
        
        print(f'-> {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {situacao}')
    
    menu()

def alterar_estadoRestaurante():
    mostrar_subtitulo("Alterar situação do restaurante")
    nome_restaurante = input("Digite o nome do restaurante que deseja alterar: ")
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso!" if restaurante['ativo'] else f"O restaurante {nome_restaurante} foi desativado com sucesso!"
            print(mensagem)
    if not restaurante_encontrado:
        print ("Restaurante não encontrado!")
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
            alterar_estadoRestaurante()
        
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