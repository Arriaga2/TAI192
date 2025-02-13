from fastapi import FastAPI, HTTPException
from typing import Optional


app = FastAPI(
    title='API Repaso S-192',
    description='Creado Por Jelipe',
    version='1.0.1'
)



tareas = [
    {"id": 1, "titulo": "Comprar víveres", "descripcion": "Comprar leche y pan", "vencimiento": "15-02-24", "estado": "no completada"},
    {"id": 2, "titulo": "Estudiar para el examen", "descripcion": "Repasar los apuntes de matemáticas", "vencimiento": "16-02-24", "estado": "no completada"},
    {"id": 3, "titulo": "Hacer ejercicio", "descripcion": "Correr 5 km en el parque", "vencimiento": "17-02-24", "estado": "no completada"},
    {"id": 4, "titulo": "Leer un libro", "descripcion": "Terminar el capítulo 4 de El Principito", "vencimiento": "18-02-24", "estado": "no completada"},
    {"id": 5, "titulo": "Llamar a mamá", "descripcion": "Hablar con mamá por videollamada", "vencimiento": "19-02-24", "estado": "no completada"}
]


# Endpoint home
@app.get('/', tags=['Calando el rollo'])
def home():
    return {'hello': 'world FastAPI'}


