num = int(input("Informe um número: "))
print(f"Opa! Vou mostrar a tabuada do {num} para você \n")

print("==============")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
print("==============")