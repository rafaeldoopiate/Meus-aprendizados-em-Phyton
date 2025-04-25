notas=[]
contador = 0

while contador<5:
    notas.append(float(input(f"Informe a {contador} a nota ")))
    contador+=1

maiornotas=max(notas)
menornotas=min(notas)
media=sum(notas)/ len(notas)

print(f"\nA média total é {media:.2f}")
print(f"A maior nota é {maiornotas}")
print(f"A menor nota é {menornotas}")

if media>=7:
    print("APROVADO")
else:
    print(f"REPROVADO: com a média{media}")
