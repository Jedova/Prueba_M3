# Construir lógica para escoger el nivel...
# nivel: basicas, intermedias, avanzadas (0,1,2)
# p_level: cuántas preguntas hay por nivel (1,2 o 3)

def choose_level(n_pregunta, p_level):
    numero_preg=[1,2,3]
    nivel_complex=[0,1,2]
    if p_level not in numero_preg:
           print(f"El n° de preguntas debe ser 1, 2 o 3, no {p_level}")
    if n_pregunta not in nivel_complex:
        print(f"El nivel de complejidad debe clasificarse como 0, 1 o 2, no {n_pregunta}")
        return[] ## se aplica para que entregue None ya que se tuvo problemas dejandolo abierto, sin return
    inicio = n_pregunta * p_level + 1 ## se establecen los parámetros del rango
    fin = inicio + p_level - 1

    return list(range(inicio, fin + 1))

if __name__ == "__main__": # evaluación del código
    
    preguntas = int(input("¿Cuántas preguntas deseas por nivel (1,2 o 3)?: "))
    nivel  = int(input("¿Qué nivel? 0=básicas, 1=intermedias, 2=avanzadas: "))
    lista_num  = choose_level(nivel,preguntas)
    if lista_num:
        print(f"Nivel {nivel} con {preguntas} preguntas → preguntas a responder son: {lista_num}")
    else:
        print("No se pudieron calcular las preguntas debido a una entrada inválida")