while True:
        print("\nSelecione a operação:")
        print("1. Saudação")
        print("2. Perguntar como está")
        print("3. Oferecer ajuda")
        print("4. Notícias")
        print("5. Sair")

        escolha = input("Digite o número da operação desejada: ")
    
        if escolha == "1":
            print("Olá Usuário")
            
        elif escolha == "2":
            print("Tudo bem?")
            
        elif escolha == "3":
            print("No que eu posso te ajudar hoje?")
            
        elif escolha == "4":
            print("Quer saber as novas notícias?")
             
        elif escolha == "5":
            print("Encerrando o programa...") 
            
        else:
            print("\nOpção inválida. Tente novamente.")