

nota1=float(input("escreva sua primeira nota"))
nota2=float(input("escreva sua segunda nota"))
nota3=float(input("escreva sua segunda nota"))

media=(nota1+nota2+nota3)/3
if media >=7:
    print("aprovado:")

    if media<4:
     print("recuperação")
    else:
     print("reprovado")