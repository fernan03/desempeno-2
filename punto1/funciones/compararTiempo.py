def compararTiempo(listaCiclistas):
    tiempoMenor=listaCiclistas[0]['tiempo']
    nombre=listaCiclistas[0]['nombre']

    for ciclista in listaCiclistas:
        if ciclista['tiempo'] < tiempoMenor:
            tiempoMenor=ciclista['tiempo']
            nombre=ciclista['nombre']

    print(f'el tiempo menor fue: {tiempoMenor} horas, por parde de {nombre}')
    