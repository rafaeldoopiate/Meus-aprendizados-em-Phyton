import json

def carregar_alimentos():
    try:
        with open("alimentos.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def salvar_alimentos(lista_alimentos):
    with open("livros.json", "w") as arquivo:
        json.dump(lista_alimentos, arquivo, indent=4)

def add_lista(lista_alimentos):
    titulo = input("Digite o nome do alimento: ")
    q = input("Digite o número de alimento: ")
    alimento = {"Alimento": titulo, "Quantidade": q}
    lista_alimentos.append(alimento)
    print(f" Alimento '{titulo}' adicionado com sucesso!")

def listar_alimentos(lista_alimentos):
    if not lista_alimentos:
        print("Nao ha Alimentos cadastrados.")
        return
    print("\n--- Lista de Alimentos ---")
    for i, alimento in enumerate(lista_alimentos):
        print(f"{i+1}. {alimento}")
    print("-----------------------\n")

def remove_alimentos(lista_alimentos):
    if not lista_alimentos:
        print("Nao ha Alimentos para remover.")
        return
    listar_alimentos(lista_alimentos)
    try:
        indice_str = input("Digite o numero do livro que deseja remover: ")
        if not indice_str.isdigit():
            print("Entrada invalida. Digite um numero.")
            return
        indice = int(indice_str) - 1
        if 0 <= indice < len(lista_alimentos):
            remove_alimentos = lista_alimentos.pop(indice)
            print(f"Alimento '{remove_alimentos}' removido com sucesso!")
        else:
            print("indice invalido.")
    except ValueError:
        print("Erro ao processar a entrada.")

def buscar_alimentos(lista_alimentos):
            if not lista_alimentos:
                print("Nao ha livros cadastrados para buscar.")
                return

            termo_busca = input("Digite o titulo ou autor para buscar: ").lower()
            resultados = []
            for alimento in lista_alimentos:
                if termo_busca in alimento['titulo'].lower() or termo_busca in alimento['autor'].lower():
                    resultados.append(alimento)

            if resultados:
                print("\n--- Resultados da Busca ---")
                for i, alimento in enumerate(resultados):
                    print(f"{i+1}. {alimento}")
                print("---------------------------\n")
            else:
                print("Nenhum livro encontrado com esse termo.")

def editar_alimento(lista_alimento):
    if not lista_alimento:
        print("Nao ha livros para editar.")
        return

    listar_alimentos(lista_alimento)
    try:
        indice_str = input("Digite o numero do livro que deseja editar: ")
        if not indice_str.isdigit():
            print("Entrada invalida. Digite um numero.")
            return
        indice = int(indice_str) - 1
        if 0 <= indice < len(lista_alimento):
            livro = lista_alimento[indice]
            print(f"\nEditando o livro: '{livro['titulo']}' de '{livro['autor']}'")
            novo_titulo = input(f"Novo titulo (deixe em branco para manter '{livro['titulo']}'): ")
            novo_autor = input(f"Novo autor (deixe em branco para manter '{livro['autor']}'): ")

            if novo_titulo:
                livro['titulo'] = novo_titulo
            if novo_autor:
                livro['autor'] = novo_autor

            print("Livro editado com sucesso!")
        else:
            print("Indice invalido.")
    except ValueError:
        print("Erro ao processar a entrada.")

def exibir_menu():
    print("\n--- Menu de Cadastro de Alimentos ---")
    print("1. Adicionar Alimentos")
    print("2. Listar Alimentos")
    print("3. Remover Alimentos")
    print("4. Buscar Alimentos ")
    print("5. Editar Livro ")
    print("6. Encerrando Programa....")
    print("-----------------------------------\n")

def main():
    lista_alimentos = carregar_alimentos()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opcao: ")

        if opcao == '1':
            add_lista(lista_alimentos)
        elif opcao == '2':
            listar_alimentos(lista_alimentos)
        elif opcao == '3':
            remove_alimentos(lista_alimentos)
        elif opcao == '4':
            buscar_alimentos(lista_alimentos)
        elif opcao == '5':
            editar_alimento(lista_alimentos)
            salvar_alimentos(lista_alimentos)
        elif opcao == '6':
            print("Saindo do programa.")
            break
        else:
            print("Opcao invalida. Tente novamente.")

if __name__ == "__main__":
    main()