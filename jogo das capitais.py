import random

facil = {
  "Brasil": "Brasília",
  "Argentina": "Buenos Aires",
  "Estados Unidos": "Washington, D.C.",
  "França": "Paris",
  "Reino Unido": "Londres",
  "Itália": "Roma",
  "Japão": "Tóquio",
  "Alemanha": "Berlim",
  "México": "Cidade do México",
  "Canadá": "Ottawa"
}

medio = {
  "Egito": "Cairo",
  "Austrália": "Canberra",
  "Índia": "Nova Délhi",
  "África do Sul": "Pretória",
  "China": "Pequim",
  "Coreia do Sul": "Seul",
  "Portugal": "Lisboa",
  "Suécia": "Estocolmo",
  "Espanha": "Madri",
  "Rússia": "Moscou"
}

dificil = {
  "Croácia": "Zagreb",
  "Hungria": "Budapeste",
  "Mianmar": "Naypyidaw",
  "Filipinas": "Manila",
  "Nova Zelândia": "Wellington",
  "Islândia": "Reykjavik",
  "Cazaquistão": "Astana",
  "Finlândia": "Helsinque",
  "Mongólia": "Ulaanbaatar",
  "Camarões": "Yaoundé"
}


def jogar(perguntas):
    pontos = 0
    paises = list(perguntas.keys())
    random.shuffle(paises)


  
    for pais in paises:
        resposta = input(f"\nQual é a capital deste {pais}? ")
        if resposta.lower() == perguntas[pais].lower():
            pontos+=1
            print("Resposta CORRETA")
            print(f"A sua pontuação é: {pontos}")
        elif resposta.lower() != perguntas[pais].lower(): 
            print("Resposta errada")
                
def menu():
    print("\n---------------------------JOGO DAS CAPITAIS------------------------------------\n")
    print("1. Nível FACÍL")
    print("2. Nível MÉDIO")
    print("3. Nível DIFICIL")
    print("4. Sair")
    escolha = input("Escolha o nível do jogo: ")

    if escolha == "1":
        jogar(facil)
    elif escolha == "2":
        jogar(medio)
    elif escolha == "3":
        jogar(dificil)
    elif escolha == "4":
        print("Saindo do jogo. Até a próxima!")
    else:
        print("Opção inválida. Tente novamente.")
        menu()
        
menu()




