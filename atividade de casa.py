hora1 = int(input("Digite a hora 1: "))
minuto1 = int(input("Digite o minuto 1: "))
hora2 = int(input("Digite a hora 2: "))
minuto2 = int(input("Digite o minuto 2: "))


minutosaida = minuto1 + minuto2
horasaida = hora1 + hora2


if minutosaida >= 60:
    horasaida += 1
    minutosaida -= 60

if horasaida >= 24:
    horasaida -= 24

if horasaida >= 12:
    horasaida -= 12


print(f"{horasaida}:{minutosaida:02d}")