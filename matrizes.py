cadastros=[]
while True:
    
    print("\nSelecione a operação:")
    print("1. Digite seu nome, idade e endereço")
    print("2. Listar")
    print("3. Sair")
    escolha = input("\nDigite o número da operação desejada: ")

    if escolha == "1": 

        nome= input("\nDigite seu nome: ")  
        idade= int(input("Digite sua idade: "))
        e = input("Digite seu endereço: ")
        cadastro = nome, idade, e
        cadastros.append(cadastro)



    elif escolha == "2":
        for cadastro in cadastros:
            print(f"{cadastro}")

    elif escolha == "3":
          print("Encerrando programa...")
          break