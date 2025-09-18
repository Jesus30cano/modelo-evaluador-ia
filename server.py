from fastapi import FastAPI
from pydantic import BaseModel
from evaluador_semantico import evaluar_respuesta

app = FastAPI()

class Peticion(BaseModel):
    pregunta: str
    respuesta: str

@app.post("/evaluar")
def evaluar(peticion: Peticion):
    return evaluar_respuesta("respuestas.csv", peticion.pregunta, peticion.respuesta)
