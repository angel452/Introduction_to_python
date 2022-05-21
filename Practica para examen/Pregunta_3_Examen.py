print("Responda con si o no")
respuesta=str(input("El carro enciende?: "))
if respuesta == "si":
    print("No existe ningun problema")
else:
    respuesta_2 = str(input("¿Tiene llave en la mano?: "))
    if respuesta_2 == "no":
        print("Busque la llave")        
    else:
        respuesta_3 = str(input("¿Introdujo la llave?: "))
        if respuesta_3 =="no":
            print("Introdusca la llave")
        else:
            respuesta_4 = str(input("¿Cambio el selector de cambio?: "))
            if respuesta_4 == "no":
                print("Cambie el selector")
            else:
                print("Gire la llave de contacto para arrancar el automovil")