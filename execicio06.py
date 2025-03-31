visitante=int(input("time1:"))
mandante=int(input("time2: "))

gols_visitantes=int(input("soldos de gols:"))
gols_mandantes=int(input("saldos de gols:"))

if gols_mandantes > gols_visitantes:
     print(f"vitoria dos {mandante}")

else:
      if gols_visitantes>gols_mandantes:

          print(f"vitoria do {mandante}")

      else:
            print("houve um empate entre os 2 times")


