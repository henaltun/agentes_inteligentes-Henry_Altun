import random

def recomendar_pelicula(genero):
    """Devuelve una película recomendada según el género ingresado."""
    peliculas = {
        "accion": ["Mad Max: Fury Road", "John Wick", "Gladiador", "Misión Imposible"],
        "comedia": ["Superbad", "La máscara", "Dumb and Dumber", "The Hangover"],
        "drama": ["Forrest Gump", "El Padrino", "Titanic", "El club de la pelea"],
        "ciencia ficcion": ["Interestelar", "Blade Runner 2049", "Matrix", "Star Wars"]
    }
    
    genero = genero.lower()
    if genero in peliculas:
        return random.choice(peliculas[genero])
    else:
        return "Lo siento, no tenemos recomendaciones para ese género."

# Solicitar género al usuario
if __name__ == "__main__":
    print("Ingrese su género de película favorito (acción, comedia, drama, ciencia ficción):")
    genero_usuario = input("Género: ")
    recomendacion = recomendar_pelicula(genero_usuario)
    print(f"Recomendación: {recomendacion}")