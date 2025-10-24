nota1 = float(input("Introduce la nota del primer examen:"))
notaEsperada = float(input("Introduce que esperar sacar en el trimestre:"))

nota1 *= 0.4

nota2 = (notaEsperada - nota1) / 0.6

print('Para tener un ' , notaEsperada , ' en el trimestre necesitas sacar un ' , nota2 , ' en el segundo examen')