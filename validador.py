
def validate(opciones, eleccion):
    # Definir validación de eleccion
   while eleccion not in opciones: ##se crea un mientras elección no este en opciones
        print(f"Opción no válida, ingrese una de las opciones válidas: {opciones}") ## entrega error y devuelve al bucle
        eleccion = input("mi respuesta es: ") ##solicita incluir respuesta
   return eleccion

if __name__ == "__main__": ##permite probar manualmente pero evita que se exporte el código desde la página main
    
    eleccion = input("Ingresa una Opción: ").lower()
    letras = ["a","b","c","d"]
    correcto = validate(letras, eleccion) ##crea la variable de validación
    print (f"Elección válida: {correcto}") ##permite imprimir el valor para que el usuario tenga feedback
    
