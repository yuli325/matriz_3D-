Iteración de arreglos multidimensionales con bucles anidados
Crear una matriz 3D que represente los datos de temperaturas diarias en varias ciudades. En una dimensión, puedes tener diferentes ciudades, en otra dimensión, días de la semana (Lunes, Martes, Miércoles, etc.), y en la tercera dimensión, semanas.
Dentro de cada celda de la matriz, puedes almacenar las temperaturas diarias para una ciudad en un día específico de una semana determinada.
Utilizar bucles anidados para calcular el promedio de temperaturas para una ciudad por cada una de las semanas.
Mostrar el promedio de temperaturas para cada ciudad y semana en la pantalla.
temperaturas = [
    [   # Tena
        [   # Semana 1
            {"day": "Lunes", "temp": 25},
            {"day": "Martes", "temp": 27},
            {"day": "Miércoles", "temp": 26},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 32}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 26},
            {"day": "Martes", "temp": 28},
            {"day": "Miércoles", "temp": 27},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 31},
            {"day": "Sábado", "temp": 33},
            {"day": "Domingo", "temp": 34}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 25},
            {"day": "Martes", "temp": 29},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 34},
            {"day": "Domingo", "temp": 35}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 26},
            {"day": "Martes", "temp": 27},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 33},
            {"day": "Sábado", "temp": 34},
            {"day": "Domingo", "temp": 35}
        ]
    ],
    [   # Puyo
        [   # Semana 1
            {"day": "Lunes", "temp": 25},
            {"day": "Martes", "temp": 26},
            {"day": "Miércoles", "temp": 27},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 31}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 26},
            {"day": "Martes", "temp": 27},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 32},
            {"day": "Domingo", "temp": 33}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 27},
            {"day": "Martes", "temp": 28},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 33},
            {"day": "Domingo", "temp": 34}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 29},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 34},
            {"day": "Domingo", "temp": 35}
        ]
    ],
    [   # Quito
        [   # Semana 1
            {"day": "Lunes", "temp": 26},
            {"day": "Martes", "temp": 27},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 32}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 27},
            {"day": "Martes", "temp": 28},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 31},
            {"day": "Sábado", "temp": 32},
            {"day": "Domingo", "temp": 33}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 29},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 33},
            {"day": "Domingo", "temp": 34}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 31},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 33},
            {"day": "Sábado", "temp": 34},
            {"day": "Domingo", "temp": 35}
        ]
    ]
]

nombres_ciudades = ["Tena", "Puyo", "Quito"]

# Calcular el promedio de temperaturas para cada ciudad y semana
for index, ciudad in enumerate(temperaturas):
    print(f"Ciudad: {nombres_ciudades[index]}")
    for semana_index, semana in enumerate(ciudad):
        suma = 0
        conteo = 0
        for dia in semana:
            suma += dia['temp']
            conteo += 1
        promedio = suma / conteo
        print(f"  Promedio Semana {semana_index + 1}: {promedio:.2f}")
