def mostrar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        print("Tarefas:")
        for i, tarefa in enumerate(tarefas, 1):
            status = "✔" if tarefa[1] else "✘"
            print(f"{i}. [{status}] {tarefa[0]}")

def adicionar_tarefa(tarefas):
    desc = input("Descrição da tarefa: ").strip()
    if desc:
        tarefas.append([desc, False])
        print("Tarefa adicionada!")
    else:
        print("Descrição vazia!")

def marcar_concluida(tarefas):
    mostrar_tarefas(tarefas)
    if not tarefas:
        return
    try:
        n = int(input("Número da tarefa para marcar como concluída: "))
        if 1 <= n <= len(tarefas):
            tarefas[n-1][1] = True
            print("Tarefa marcada!")
        else:
            print("Número inválido.")
    except:
        print("Entrada inválida.")

def menu():
    tarefas = []
    while True:
        print("""
1 - Listar tarefas
2 - Adicionar tarefa
3 - Marcar tarefa como concluída
0 - Sair
""")
        op = input("Escolha: ")
        if op == '1':
            mostrar_tarefas(tarefas)
        elif op == '2':
            adicionar_tarefa(tarefas)
        elif op == '3':
            marcar_concluida(tarefas)
        elif op == '0':
            print("Tchau! Até mais!")
            break
        else:
            print("Opção inválida!")

if __name__ == '__main__':
    menu()
