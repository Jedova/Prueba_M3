import preguntas as p


def verificar(alternativas, eleccion):
    eleccion = ["a", "b", "c","d"].index(eleccion) #devuelve el índice de elección dada
    correcto = alternativas[eleccion][1] == 1 # generar lógica para determinar respuestas correctas
    return correcto

if __name__ == "__main__":
    from print_preguntas import print_pregunta
    # Siempre que se escoja la alternativa con alt_2 estará correcta, e incorrecta en cualquier otro caso
    pregunta = p.pool_preguntas["basicas"]["pregunta_2"]
    print_pregunta(pregunta["enunciado"],pregunta["alternativas"])
    respuesta = input("Escoja la alternativa correcta:\n> ").lower()
    verificar(pregunta["alternativas"], respuesta)






