estudante = input("É estudante? (sim/não): ")
dia = input("Qual dia da semana é? (segunda-feira, terça-feira, etc.): ")
sala = input("Qual é o tipo de sala? (Vip ou comum): ")

if estudante == "sim" and dia == "terça-feira" and sala == "comum":
    print("Desconto Aplicado")
else:
    print("Valor Integral") 