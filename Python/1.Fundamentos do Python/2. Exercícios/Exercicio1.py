cadastro = [{'nome': 'Vitor', 'idade': '19', 'cidade': 'Santo Andre'},
            {'nome': 'Luise', 'idade': '18', 'cidade': 'Santo Andre'},
            {'nome': 'Henrique', 'idade': '17', 'cidade': 'Santo Andre'}]

def atualizarNome():
    print("Atualização de idade")
    name = input("Digite o nome da pessoa que deseja alterar o nome: ")
    encontrado = False
    for pessoa in cadastro: 
        if name == pessoa['nome']:
            print("A pessoa foi encontrada em nosso sistema")
            encontrado = True
            nidade = input("Digite a idade atualizada: ")
            print(f"A idade de {name} foi alterada para {nidade}")
            pessoa["idade"] = nidade
            break
    if not encontrado: print("A pessoa não foi encontrada em nosso sistema")

if __name__ == '__main__':
    atualizarNome()