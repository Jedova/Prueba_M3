import preguntas as p
import random
from shuffle import shuffle_alt

# Opciones dadas para escoger.
opciones = {'basicas': [1,2,3],
            'intermedias': [1,2,3],
            'avanzadas': [1,2,3]}

def choose_q(dificultad):
    global opciones ##permite modificar el diccionario global
    if not opciones[dificultad]:
        raise ValueError(f"No quedan preguntas disponibles para el nivel {dificultad}")
    # escoger una pregunta
    n_elegido = random.choice(opciones[dificultad])
    opciones[dificultad].remove(n_elegido)

    clave_pregunta = f"pregunta_{n_elegido}"  # Permite obtener la pregunta correspondiente
    pregunta = p.pool_preguntas[dificultad][clave_pregunta]

    alternativas = shuffle_alt(pregunta) # Se utiliza para mezclar alternativas

    return pregunta['enunciado'][0], alternativas


if __name__ == '__main__':
    # si ejecuto el programa, las preguntas cambian de orden, pero nunca debieran repetirse
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    