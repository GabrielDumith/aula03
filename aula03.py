nome= input("escreva seu nome: ")
idade= int(input("escreva sua a idade: "))
salario= float(input("escreva o seu salario: "))
aumento= int(input("escreva o seu aumento: "))

money= (salario*aumento)/100

novo_salario=(salario+money)

print(f"seu nome é:{nome}, sua idade:{idade}, salario{salario}"
      f"seu novo salario{novo_salario}")


