from fastapi import FastAPI
from typing import Optional

app = FastAPI(
    title='My FastAPI 192', 
    description='API de Jelipe',
    version='1.0.1',
)

usuarios=[
    {"id":1,"nombre":"Jelipe","edad":20},
    {"id":2,"nombre":"Kevin","edad":23},
    {"id":3,"nombre":"Manlio","edad":26},
    {"id":4,"nombre":"Mari","edad":29}
]

# Endpoint home
@app.get('/', tags=['Hola Mundo'])
def home():
    return {'hello': 'world FastAPI'}


#endpoint parametro obligatorio
@app.get('/usuario/{id}', tags=['Parametro obligatorio'])
def consultaUsuario(id:int):
    #conexion a la BD
    #consultamos
    return {'Se encontró el usuario':id}

# Endpoint con parámetro opcional
@app.get('/usuario/', tags=['Parametro Opcional'])
def consulta_usuario_opcional(usuario_id: Optional[int] = None):
    if usuario_id is not None:
        for usuario in usuarios:
            if usuario["id"] == usuario_id:
                return {"Mensaje": "Usuario encontrado", "Usuario": usuario}
        return {"Mensaje": f"No se encontró el usuario con id: {usuario_id}"}
    else:
        return {'Mensaje': "No se proporcionó un id"}