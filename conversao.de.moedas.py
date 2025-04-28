conversao=[]
while True:

    print("---------- Menu de Conversão ---------- ")
    print("1. Real para Dólar")
    print("2. Dólar para Real")
    print("3. Euro para Real")
    print("4. Real para Euro")
    print("5. Sair")
    escolha = input("\nSelecione a operação: ")

    if escolha == "1":
        num = float(input("\nDigite o valor em REAL: : "))
        print(f"{num*0,196} dólares")
    elif escolha == "2":
        num = float(input("\nDigite o valor em DÓLAR: : "))
        print(f"{num*5.67} reais")
    elif escolha == "3":
        num = float(input("\nDigite o valor em EURO: : "))
        print(f"{num*0,1610} reais")
    if escolha == "4":
        num = float(input("\nDigite o valor em REAL: : "))
        print(f"{num*6.47} euros")
    if escolha == "5":
        print("Encerrando o Programa....")
        break
    else:
            print("Opção inválida. Tente novamente.")