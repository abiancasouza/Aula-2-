idade = int(input("Digite sua idade: "))
altura = int(input("Digite sua altura: "))
autorizacao = int(input("Tem autorização dos pais? (sim/não): "))

if autorizacao == "sim" and idade >=140 and idade <= 12:
    print ("Aceso Liberado")
else:
    print("Acesso Negado")
