from esUnitaria import esUnitaria

def prueba(M):
    if esUnitaria(M):
        print("Si es unitaria")
    else:
        print("No es unitaria")

Z = [[2, 0, 0], [0, 2, 0], [0, 0, 2]]

prueba(Z)
