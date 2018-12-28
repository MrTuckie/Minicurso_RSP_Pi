# Código feito por Arthur Lorencini Bergamaschi

soma = 0
i = 0

for x in range(1,6):
    a = input("Digite a nota #%d\n" % x)
    a = float(a)
    soma += a # Equivale a soma = soma + a
    i += 1

media = soma/i
print("A média foi de %.2f" % media)
