n = int(input("digite o numero: "))

# soma = 0
# for i in range(0, n+1):
#     if i % 2 != 0:
#         soma += i
#
# print(f"a soma de todos os numeros impars até {n} é {soma}")

result = (
    [i+i for i in range(0, n+1) if i % 2 != 0]
)


for x in range(0, 50):
    print(x)