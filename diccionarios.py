#Los diccionarios son variables especiales
#que me permiten almacenar multiples datos
#de diferente TIPO EN UNA SOLA VARIABLE

empleado={
    'nombre':"Juan",
    'cedula':1017170603,
    'cargo':"Analista de datos",
    'salario':8000000,
    'horasTrabajadas':40,
    'aplicaSubsidioTransporte':False,
    'deudas':[1500000,800000],
    
}
#print (empleado)
#print(empleado['deudas'][1])


#RECORRIENDO UN DICCIONARIO:
for observadorAtributo,observadorValor in empleado.items():
    print(observadorValor)