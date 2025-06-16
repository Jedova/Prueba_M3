import preguntas as p
import random
from shuffle import shuffle_alt

# Opciones dadas para escoger.
opciones = {
    "basicas": list(p.pool_preguntas["basicas"].values()),
    "intermedias": list(p.pool_preguntas["intermedias"].values()),
    "avanzadas": list(p.pool_preguntas["avanzadas"].values())
}

def choose_q(dificultad):
    global opciones
    if not opciones[dificultad]:
        raise ValueError(f"No quedan preguntas disponibles para el nivel {dificultad}")
    
    pregunta = random.choice(opciones[dificultad])
    opciones[dificultad].remove(pregunta)

    alternativas = shuffle_alt(pregunta)
    return pregunta['enunciado'][0], alternativas


if __name__ == '__main__':
    # si ejecuto el programa, las preguntas cambian de orden, pero nunca debieran repetirse
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    