print("Hello, World!")

nome= input("Digite seu nome: ")
idade= int(input("Digite sua idade: "))
print(f"Olá, {nome}, sua idade é {idade}")

n1 = int(input("\nDigite um número "))
n2 = int(input("Digite um número "))
soma = n1+n2
print("\nA soma dos números {} e {} é {}".format(n1, n2, soma))

if soma>10:
    print(f"{soma} é maior que 10")
else:
    print(f"{soma} é menor que 10")