print("=== Juego: Piedra, Papel o Tijera ===")

jugador1 = input("Jugador 1, elige piedra, papel o tijera: ").strip().lower()
jugador2 = input("Jugador 2, elige piedra, papel o tijera: ").strip().lower()

opciones_validas = ["piedra", "papel", "tijera"]

if jugador1 not in opciones_validas or jugador2 not in opciones_validas:
    print("Error: alguna de las opciones introducidas no es válida.")
else:
    if jugador1 == jugador2:
        print("Empate.")
    elif (jugador1 == "piedra" and jugador2 == "tijera") or \
         (jugador1 == "papel" and jugador2 == "piedra") or \
         (jugador1 == "tijera" and jugador2 == "papel"):
        print("¡Gana el Jugador 1!")
    else:
        print("¡Gana el Jugador 2!")
