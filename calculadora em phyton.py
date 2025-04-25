def cal():
    continuar = True
    while continuar:
        print("\nSelecione a operação:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")
        escolha = input("Digite o número da operação desejada: ")

        if escolha in ('1', '2', '3', '4'):
            try: 
                n1 = float(input("Digite o primeiro número: "))
                n2 = float(input("Digite o segundo número: "))

                if escolha == '1':
                    print(f"{n1} + {n2} = {n1 + n2}")
                elif escolha == '2':
                    print(f"{n1} - {n2} = {n1 - n2}")
                elif escolha == '3':
                    print(f"{n1} * {n2} = {n1 * n2}")
                elif escolha == '4':
                    if n2 == 0:
                        print("Erro: divisão por zero não é permitida.")
                    else:
                        print(f"{n1} / {n2} = {n1 / n2}")
            except ValueError:
                print("Entrada inválida. Por favor, insira números válidos.")
                
        elif escolha == '5':
            print("Calculadora encerrada.")
            continuar = False
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    cal()