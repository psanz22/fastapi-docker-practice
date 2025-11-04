from fastapi import FastAPI
import random
import math 

app = FastAPI()

target_number = None
remaining_attempts = 0
lower = 0
upper = 0

@app.get("/")
def hello():
    return {"message": "This is fastapi with docker practice! 🚀🚀🚀"}

@app.post("/start_game")
def start_game(start_lower: int, start_upper: int):
    global lower, upper, target_number, remaining_attempts

    lower = start_lower
    upper = start_upper
    
    target_number = random.randint(lower, upper)

    remaining_attempts = math.ceil(math.log2(upper - lower + 1)) #el logaritmo base 2 te dice cuántas veces puedes dividir el rango a la mitad antes de encontrar el número

    return {
        "message": f"El juego ha comenzado. Busca un número entre {lower} y {upper}. Tienes {remaining_attempts} intentos, motherfucker."
    }

@app.post("/guess")
def make_guess(guess: int):
    global remaining_attempts, target_number

    if target_number is None:
        return {"message": "Primero inicia el juego con /start_game."}
    
    if remaining_attempts <= 0:
        return {"message": "Has perdido pringáááá, era {target_number} JA-JA"}
    
    remaining_attempts -= 1 #esto es lo mismo que escribir remaining_attempts = remaining_attempts -1

    if guess == target_number:
        respuesta = "¡Anda! ¡Lo has adivinado! Qué lista..."
        target_number = None
        return {"message": respuesta}
    elif guess > target_number:
        return {"message": f"Te pasaste, webona. Te quedan {remaining_attempts} intentos."}
    else:
        return {"message": f"Te quedaste corta, muyaya. Te quedan {remaining_attempts} intentos."}

