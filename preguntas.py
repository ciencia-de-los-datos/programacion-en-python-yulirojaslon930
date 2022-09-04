"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

def upload_data ():
    import csv
    with open('data.csv', 'r') as file:
        data = file.readlines()
        data = [line.replace("\n","") for line in data]
        data = [line.split("\t") for line in data]
    return data


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    data = upload_data()
    # print(data)
    suma = 0
    for lista in data:
        suma = int(lista[1]) + suma
        # print(lista[1], ' => ', suma)
    return suma

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    data = upload_data()

    counter= {}
    for lista in data:
        if lista[0] in counter:
            counter[lista[0]] += 1
        else:
            counter[lista[0]] = 1
    varfinal =[(letra, counter[letra]) for letra in counter]
    varfinal.sort(key = lambda x: x[0])
    return varfinal

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    data = upload_data()
    
    counter= {}
    for lista in data:
        if lista[0] in counter:
            counter[lista[0]] += int(lista[1])
        else:
            counter[lista[0]] = int(lista[1])
    varfinal =[(letra, counter[letra]) for letra in counter]
    varfinal.sort(key = lambda x: x[0])
    return varfinal  


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    data = upload_data()
    counter = {}
    for lista in data:
        fecha = lista[2]
        mes = fecha.split("-")
        if mes[1] in counter:
            counter[mes[1]] += 1
        else:
            counter[mes[1]] = 1
    conteo_final = [(contmes,counter[contmes] ) for contmes in counter]
    conteo_final.sort(key = lambda x: x[0])
    return conteo_final


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    data = upload_data()
    
    diccionario_min ={}
    diccionario_max ={}
    
    for lista in data:
        if lista[0] in diccionario_min:
            if int(lista[1]) < diccionario_min[lista[0]]:
                diccionario_min[lista[0]] = int(lista[1])
        elif lista[0] not in diccionario_min:
            diccionario_min[lista[0]] = int(lista[1])
        if lista [0] in diccionario_max:
            if int(lista[1]) > diccionario_max[lista[0]]:
                diccionario_max[lista[0]] = int(lista[1])
        elif lista[0] not in diccionario_max:
            diccionario_max[lista[0]] = int(lista[1])
    list_result =[]
    for result in zip(diccionario_max.keys(),list(diccionario_max.values()),list(diccionario_min.values())):
        list_result.append(result)
        list_result.sort(key = lambda x: x[0])
    return list_result

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    
    data = upload_data ()
    
    
    diccionario_min = {}
    diccionario_max = {}
    for row in data:
        data = row[4].split(",")
        for element in data:
            key = element[:3]
            value = int(element[4:])
            if key in diccionario_min:
                if value < diccionario_min[key]:
                    diccionario_min[key] = value
            elif key not in diccionario_min:
                diccionario_min[key] = value
            if key in diccionario_max:
                if value > diccionario_max[key]:
                    diccionario_max[key] = value
            elif key not in diccionario_max:
                diccionario_max[key] = value           
    list_result =[]
    for result in zip(diccionario_min.keys(),list(diccionario_min.values()),list(diccionario_max.values())):
        list_result.append(result)
        list_result.sort(key = lambda x: x[0])
    return list_result


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    data = upload_data ()
    
    diccionario ={}
    
    
    for key in data:
        if int(key[1]) not in diccionario:
            diccionario[int(key[1])]= [key[0]]
        else: 
            list= diccionario[int(key[1])]
            list.append(key[0])
            diccionario[int(key[1])] = list
    
    list_result = [(key, diccionario[key]) for key in diccionario]
    list_result.sort(key=lambda x: x[0])
    return list_result

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    data = upload_data ()
    
    diccionario ={}
    
    for key in data:
        if int(key[1]) not in diccionario:
            diccionario[int(key[1])]= [key[0]]
        else: 
            list= diccionario[int(key[1])]
            list.append(key[0])
            diccionario[int(key[1])] = list
    
    for x in diccionario:
        z = []
        for y in diccionario[x]:
            if y not in z:
                z.append(y) # añade un elemento a la lista
        z = sorted(z)   # ordenar listas, tuplas, diccionarios 
        diccionario[x] = z
    
    list_result = [(key, diccionario[key]) for key in diccionario]
    list_result.sort(key=lambda x: x[0])
    return list_result


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    data = upload_data ()
    
    diccionario ={}
    
    for lista in data:
        data = lista[4].split(",")
        for key in data:
            variable = key[:3]
            if variable not in diccionario:
                diccionario[variable] = 1
            else: 
                diccionario[variable] += 1
    diccionario = dict(sorted(diccionario.items())) # dict conviernene en diccionario una lista de tuplas y .items() en sorted ordena
    return diccionario


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    data = upload_data ()
    list = []
    for x in data:
        y = len(x[3].split(","))
        z = len(x[4].split(","))
        tupla = (x[0], y,z)
        list.append(tupla)
    print(list)
    return 0
pregunta_10 ()


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    return


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    return
