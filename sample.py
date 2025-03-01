def ingresar_puntuacion_comentario():
    while True:
        print('Por favor, introduzca una puntuación en una escala de 1 a 5')
        point = input()

        if point.isdecimal():
            point = int(point)
            if point <= 0 or point > 5:
                print('Por favor, introduzca un valor entre el 1 y 5')
            else:
                print('Por favor, introduzca un comentario')
                comment = input()
                post = f'punto: {point}, comentario: {comment}'
                with open("data.txt", 'a') as file_pc:
                    file_pc.write(f'{post}\n')
                print('¡Puntuación y comentario guardados!')
                break
        else:
            print('Por favor, introduzca la puntuación en números')

def mostrar_resultados():
    print('Resultados hasta la fecha:')
    try:
        with open("data.txt", "r") as read_file:
            resultados = read_file.read()
            if resultados:
                print(resultados)
            else:
                print('No hay puntuaciones registradas aún.')
    except FileNotFoundError:
        print('No se han registrado puntuaciones hasta ahora.')


def gestionar_seleccion():
    while True:
        print('Seleccione el proceso que desea aplicar:')
        print('1: Ingresar puntuación y comentario')
        print('2: Comprueba los resultados obtenidos hasta ahora.')
        print('3: Finalizar')
        num = input()

        if num.isdecimal():
            num = int(num)
            if num == 1:
                ingresar_puntuacion_comentario()
            elif num == 2:
                mostrar_resultados()
            elif num == 3:
                print('Finalizando')
                break
            else:
                print('Por favor, introduzca un número del 1 al 3.')
        else:
            print('Por favor, introduzca un número del 1 al 3.')

gestionar_seleccion()
