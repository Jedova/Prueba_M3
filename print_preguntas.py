import preguntas as p

def print_pregunta(enunciado, alternativas): 
    print(enunciado[0]) # Imprimir enunciado y alternativas
    letras = ["a", "b", "c", "d"]
    for i, alt in enumerate(alternativas):
        print(f"{letras[i]}. {alt}")
        
if __name__ == "__main__":
    # Las preguntas y alternativas deben mostrarse según lo indicado
    pregunta = p.pool_preguntas["basicas"]["pregunta_1"]
    print_pregunta(pregunta["enunciado"],pregunta["alternativas"])
    
    # Enunciado básico 1

    # a. alt_1
    # b. alt_2
    # c. alt_3
    # d. alt_4