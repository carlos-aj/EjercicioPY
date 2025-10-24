Lista = ["computer", "ordenador", "student", "alumno/a", "cat", "gato", "penguin", "pingüino", "machine", "maquina", "nature", "naturaleza", "light", "luz", "green", "verde", "book", "libro", "pyramid", "pirámide"]

for x in range(0,len(Lista)):
    if x % 2 == 0:
        print(f"{Lista[x]:<10}{Lista[x+1]}")