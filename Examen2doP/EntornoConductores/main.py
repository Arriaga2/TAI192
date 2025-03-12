from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel, Field
from modelsPydantic import modeloConductor

app = FastAPI(
    title='My FastAPI 192', 
    description='API de Jelipe',
    version='1.0.1',
)


# Modelo de validaciones 
class modeloConductor(BaseModel):
    nombre: str
    TipoLicencia: str
    NoLicencia: int

# Endpoint home
conductores = [
    {"nombre": "Jelipe", "TipoLicencia": "A", "NoLicencia": 12345},
    {"nombre": "Jelipe2", "TipoLicencia": "B", "NoLicencia": 12343},
    {"nombre": "Jelipe2", "TipoLicencia": "C", "NoLicencia": 12345},
    {"nombre": "Jelipe4", "TipoLicencia": "D", "NoLicencia": 12348}
]
# Endpoint CONSULTA TODOS
@app.get('/todosConductores', response_model=List[modeloConductor], tags=['Conductores'])
def leerConductores():
    return conductores

@app.get('/conductor/{NoLicencia}', tags=['ConsultaConductor'])
def consultaConductor(NoLicencia: int):
    # conexión a la BD
    return {'Se encontró el usuario': NoLicencia}

@app.put('/conductor/{NoLicencia}', response_model=modeloConductor, tags=['ActualizarConductor'])
def actualizarConductor(NoLicencia: int, conductorActualizado: modeloConductor):
    for index, usr in enumerate(conductores):
        if usr["NoLicencia"] == NoLicencia:
            conductores[index] = conductorActualizado.model_dump()
            return conductores[index]
    raise HTTPException(status_code=400, detail="El conductor no existe")

