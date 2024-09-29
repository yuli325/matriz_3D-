# Agrego información de 8 personas con datos aleatorios
informacion_personal = {
    "yuly": {"edad": 30, "ciudad": "Quito", "profesion": "diseñadora"},
    "maria": {"edad": 24, "ciudad": "Cuenca", "profesion": "ingeniera"},
    "jose": {"edad": 37, "ciudad": "Guayaquil", "profesion": "fotógrafo"},
    "lucia": {"edad": 29, "ciudad": "Ambato", "profesion": "profesora"},
    "pablo": {"edad": 21, "ciudad": "Loja", "profesion": "estudiante"},
    "sandra": {"edad": 33, "ciudad": "Manta", "profesion": "abogada"},
    "javier": {"edad": 41, "ciudad": "Machala", "profesion": "chef"},
    "ricardo": {"edad": 35, "ciudad": "Esmeraldas", "profesion": "ingeniero civil"}
}

# Imprimir información original de Yuly
print("Información original de Yuly:", informacion_personal["yuly"])

# Cambio la información de Yuly de Quito a Guayaquil
informacion_personal["yuly"]["ciudad"] = "Guayaquil"
print("Información de Yuly después de cambiar la ciudad:", informacion_personal["yuly"])

# Agregar una nueva clave-valor para la profesión de Yuly
informacion_personal["yuly"]["nueva_profesion"] = "diseñadora gráfica"
print("Información de Yuly después de agregar nueva profesión:", informacion_personal["yuly"])

# Verificar existencia de la clave "telefono"
if "telefono" not in informacion_personal["yuly"]:
    informacion_personal["yuly"]["telefono"] = "0998765432"
print("Información de Yuly después de agregar teléfono:", informacion_personal["yuly"])

# Eliminar la clave "edad"
del informacion_personal["yuly"]["edad"]
print("Información de Yuly después de eliminar la edad:", informacion_personal["yuly"])

# Imprimir el diccionario final
print("Diccionario final:", informacion_personal)

Información original de Yuly: {'edad': 30, 'ciudad': 'Quito', 'profesion': 'diseñadora'}
Información de Yuly después de cambiar la ciudad: {'edad': 30, 'ciudad': 'Guayaquil', 'profesion': 'diseñadora'}
Información de Yuly después de agregar nueva profesión: {'edad': 30, 'ciudad': 'Guayaquil', 'profesion': 'diseñadora', 'nueva_profesion': 'diseñadora gráfica'}
Información de Yuly después de agregar teléfono: {'edad': 30, 'ciudad': 'Guayaquil', 'profesion': 'diseñadora', 'nueva_profesion': 'diseñadora gráfica', 'telefono': '0998765432'}
Información de Yuly después de eliminar la edad: {'ciudad': 'Guayaquil', 'profesion': 'diseñadora', 'nueva_profesion': 'diseñadora gráfica', 'telefono': '0998765432'}
Diccionario final: {'yuly': {'ciudad': 'Guayaquil', 'profesion': 'diseñadora', 'nueva_profesion': 'diseñadora gráfica', 'telefono': '0998765432'}, 'maria': {'edad': 24, 'ciudad': 'Cuenca', 'profesion': 'ingeniera'}, 'jose': {'edad': 37, 'ciudad': 'Guayaquil', 'profesion': 'fotógrafo'}, 'lucia': {'edad': 29, 'ciudad': 'Ambato', 'profesion': 'profesora'}, 'pablo': {'edad': 21, 'ciudad': 'Loja', 'profesion': 'estudiante'}, 'sandra': {'edad': 33, 'ciudad': 'Manta', 'profesion': 'abogada'}, 'javier': {'edad': 41, 'ciudad': 'Machala', 'profesion': 'chef'}, 'ricardo': {'edad': 35, 'ciudad': 'Esmeraldas', 'profesion': 'ingeniero civil'}}
>>> 

