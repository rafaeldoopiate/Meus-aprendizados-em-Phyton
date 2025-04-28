def adicionar_livro(lista_de_livros):
    titulo = input("Digite o titulo do livro: ")
    autor = input("Digite o autor do livro: ")
    livro = {"titulo": titulo, "autor": autor}
    lista_de_livros.append(livro)
    print(f"Livro '{titulo}' adicionado com sucesso!")

def listar_livros(lista_de_livros):
    if not lista_de_livros:
        print("Nao ha livros cadastrados.")
        return
    print("\n--- Lista de Livros ---")
    for i, livro in enumerate(lista_de_livros):
        print(f"{i+1}. Titulo: {livro['titulo']}, Autor: {livro['autor']}")
    print("-----------------------\n")

def remover_livro(lista_de_livros):
    if not lista_de_livros:
        print("Nao ha livros para remover.")
        return
    listar_livros(lista_de_livros)
    try:
        indice_str = input("Digite o numero do livro que deseja remover: ")
        if not indice_str.isdigit():
            print("Entrada invalida. Digite um numero.")
            return
        indice = int(indice_str) - 1
        if 0 <= indice < len(lista_de_livros):
            livro_removido = lista_de_livros.pop(indice)
            print(f"Livro '{livro_removido['titulo']}' removido com sucesso!")
        else:
            print("indice invalido.")
    except ValueError:
        print("Erro ao processar a entrada.")

def exibir_menu():
    print("\n--- Menu de Cadastro de Livros ---")
    print("1. Adicionar Livro")
    print("2. Listar Livros")
    print("3. Remover Livro")
    print("4. Sair")
    print("-----------------------------------\n")

def main():
    lista_de_livros = []

    while True:
        exibir_menu()
        opcao = input("Escolha uma opcao: ")

        if opcao == '1':
            adicionar_livro(lista_de_livros)
        elif opcao == '2':
            listar_livros(lista_de_livros)
        elif opcao == '3':
            remover_livro(lista_de_livros)
        elif opcao == '4':
            print("Saindo do programa.")
            break
        else:
            print("Opcao invalida. Tente novamente.")

if __name__ == "__main__":
    main()