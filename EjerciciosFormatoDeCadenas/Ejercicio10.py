for i in range(9, 0, -2):
    espacios = (9 - i) // 2
    if i == 1:
        print(" " * espacios + "*")
    elif i == 9:
        print("*" * i)
    else:
        print(" " * espacios + "*" + " " * (i - 2) + "*")