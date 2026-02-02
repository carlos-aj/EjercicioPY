l = int(input())
d = int(input())
x = int(input())
lista = []

for i in range(l, d+1):
    if sum(int(digito) for digito in str(i)) == x:
        lista.append(i)

print(lista[0])
print(lista[-1])