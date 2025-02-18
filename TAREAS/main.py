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

# endpoint para obtenr todas las tareas
@app.get('/tareas', tags=['Gestion Tareas'])
def obtener_tareas():
    return {"tareas": tareas }

# endpoint para obtener una tarea especfica por ID
@app.get('/tareas/{tarea_id}', tags=['Gestion Tareas'])
def obtener_tarea(tarea_id: int):
    for tarea in tareas:
        if tarea['id'] == tarea_id:
            return {"tarea": tarea}
    raise HTTPException(status_code=404, detail="Esta taera no existe")
    
# endpoint para crear una nueva tarea
@app.post('/tareas/', tags=['Gestion Tareas'])
def crear_tarea(tarea: dict):
    for t in tareas:
        if t["id"] == tarea.get("id"):
            raise HTTPException(status_code=400, detail="El ID ya existe")
    tareas.append(tarea)
    return tarea

# endpoint para actualizar una tarea existente
@app.put('/tareas/{tarea_id}', tags=['Gestion Tareas'])
def actualizarTarea(tarea_id: int, tareaActualizada: dict):
    for index, tarea in enumerate(tareas):
        if tarea["id"] == tarea_id:
            tareas[index].update(tareaActualizada)
            return tareas[index]
    raise HTTPException(status_code=404, detail="Tarea n encontrada")

