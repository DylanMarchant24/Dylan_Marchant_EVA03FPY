from modules.data import cls, Ruta_home, ruta_json
from modules.contruccion import Enumerar_Lista, solicitar_accion

menup = ['Ver Listado de Pinturas.',
         'Buscar Pintura',
         'Agregar Pintura',
         'Eliminar Pintura',
         'Exportar Pinturas']

data = {'codigo': '',
        'nombre': '',
        'tipo': '',
        'valor': '',
        'stock': ''}

Ruta_home()
ruta_json()

while True:
    Enumerar_Lista(menup)
    resp = solicitar_accion()

    cls()
    if resp == '1':
        print(data)
    elif resp == '2':
        pass
    elif resp == '3':
        Ruta_home()
        ruta_json(__file__)
    elif resp == '4':
        pass
    elif resp == '5':
        pass
    else:
        print('Error: Opcion no valida\n')