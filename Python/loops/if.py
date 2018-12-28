# Código feito por Arthur Lorencini Bergamaschi

# Criando as variáveis
ano_a = input("Quantos anos você tem?")
ano_b = input("E quantos anos a outra pessoa tem?")

# Vendo o tipo das variáveis
print(type(ano_a))
print(type(ano_b))

# Convertendo a variável em inteiro
ano_a = int(ano_a)
ano_b = int(ano_b)

# Vendo novamente o tipo
print("depois da conversão:")
print(type(ano_a))
print(type(ano_b))

# Fazendo a comparação
if(ano_a > ano_b):
    print("A primeira pessoa é mais velha que a segunda\nDiferença de idade = %d" % (ano_a - ano_b))
elif(ano_b > ano_a):
    print("A segunda pessoa é mais velha que a primeira\nDiferença de idade = %d" % (ano_b - ano_a))
else:
    print("Vocês têm a mesma idade\n")