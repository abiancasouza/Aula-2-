Renda_mensal = float(input("Digite sua renda: "))
Score_de_credito = int(input("Digite seu score: "))
Bens_ou_Garantia = input("Você possui bens ou garantia? (sim/não): ")
Tem_historico_de_inadimplencia = input("Você tem histórico de inadimplência? (sim/não): ")

if Renda_mensal >= 3000 and Score_de_credito >= 600 and Tem_historico_de_inadimplencia == "sim" and Bens_ou_Garantia == "não":
	print("Impéstimo aprovado")
elif Tem_historico_de_inadimplencia == "não" and Bens_ou_Garantia == "sim":
	print("Impéstimo aprovado")
else:
	print("Impréstimo negado")