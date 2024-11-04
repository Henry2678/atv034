#Ler uma lista de 5 números inteiros e
#mostre cada número juntamente com a
#sua posição na lista.
lista = [int(input(f"digite um numero {i+1} ")) for i in range(5)]
for i,num in enumerate(lista):
    print(f"posicao {i}:{num} ")

