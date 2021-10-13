#En este arcchivo de definen las funciones de los calculos que despues son llamadas en la aplicación.


def sustentación_tentativa ():
    if ancho < largo:
        resultado = largo // ancho 
    else:
        resultado = ancho // largo
    
    if resultado <= 2:
        print ("Cruzada")
    else:
        print ("Rectangular")