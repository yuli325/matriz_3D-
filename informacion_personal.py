"informacion_personal"
informacion_personal = {"nombre": " Brenada Candelario","edad": "45", "ciudad":"Ambato","profesion":"Doctora"}


"ciudad"
ciudad_actual = informacion_personal["ciudad"]
print(f"Ciudad actual: {ciudad_actual}")

informacion_personal["ciudad"]= "Loja"

informacion_personal["profesion"]= "Cirujano Vascular"
if"telefono" not in informacion_personal:
    informacion_personal["telefono"] = "062322-260"

if "edad" in informacion_personal:
    del informacion_personal["edad"]
print("Diccionario final:")
print(informacion_personal)

Ciudad actual: Ambato
Diccionario final:
{'nombre': ' Brenada Candelario', 'ciudad': 'Loja', 'profesion': 'Cirujano Vascular', 'telefono': '062322-260'}

