def Enumerar_Lista(lista):
    for ind, opt in enumerate(lista):
        print(f'{ind+1}. {opt}')


def solicitar_accion():
    respuesta = input('¿Que desea hacer?:\n')
    return respuesta