gastos1 = [300,400,200,800]
gastos2 = [100,500,900,100]

total1=sum(gastos1)
total2=sum(gastos2)

print(f"{total1}")
print(f"{total2}")

if total1>total2:
    print("Os gastos 1 são maiores")
else:
    print("Os gastos 2 são maiores")