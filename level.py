# Construir lógica para escoger el nivel...
# nivel: basicas, intermedias, avanzadas (0,1,2)
# p_level: cuántas preguntas hay por nivel (1,2 o 3)

def choose_level(n_pregunta, p_level):
    niveles = ["basicas", "intermedias", "avanzadas"]
    bloque = (n_pregunta - 1) // p_level
    if bloque < 0:
        bloque = 0
    elif bloque >= len(niveles):
        bloque = len(niveles) - 1
    return niveles[bloque]

if __name__ == "__main__":
    # Prueba de retorno de niveles según el número de pregunta
    p_level = int(input("¿Cuántas preguntas por nivel (1, 2 o 3)? "))
    
    for n_pregunta in range(1, 3 * p_level + 1):
        nivel = choose_level(n_pregunta, p_level)
        print(f"Pregunta {n_pregunta} → Nivel: {nivel}")