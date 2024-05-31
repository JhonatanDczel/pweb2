from esEscalar import esEscalar

def prueba(M):
    if(esEscalar(M)):
        print("Es escalar")
    else:
        print("No es escalar")


Z = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

prueba(Z)
