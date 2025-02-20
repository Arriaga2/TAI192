from fastapi import FastAPI, HTTPException
from typing import Optional, List
from pydantic import BaseModel

app = FastAPI(
    title='My FastAPI 192', 
    description='API de Jelipe',
    version='1.0.1',
)

#modelo de validaciones 
class modeloUsuario(BaseModel):
    id: int
    nombre: str
    edad: int
    correo: str

#BD ficticia

usuarios=[
    {"id":1,"nombre":"Jelipe","edad":20,"correo":"correo1@gmail.com"},
    {"id":2,"nombre":"Kevin","edad":23,"correo":"correo2@gmail.com"},
    {"id":3,"nombre":"Manlio","edad":26,"correo":"correo3@gmail.com"},
    {"id":4,"nombre":"Mari","edad":29,"correo":"correo4@gmail.com"}
]

# Endpoint home
@app.get('/', tags=['Hola Mundo'])
def home():
    return {'hello': 'world FastAPI'}

# Endpoint CONSULTA TODOS
@app.get('/todoUsuarios', response_model= List[modeloUsuario] ,tags=['Operaciones CRUD'])
def leerUsuarios():
    return {"Los usuarios registrados son": usuarios}

# Endpoint Agregar nuevos
@app.post('/usuario/', tags=['Operaciones CRUD'])
def agregarUsuario(usuario:dict):
    for usr in usuarios:
        if usr["id"] == usuario.get("id"):
            raise HTTPException(status_code=400, detail="El ID ya existe")
    usuarios.append(usuario)
    return usuario

# Endpoint Actualizar Usuarios
@app.put('/usuario/{id}', tags=['Operaciones CRUD'])
def actualizarUsuario(id:int, usuarioActualizado:dict):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[index].update(usuarioActualizado)
            return usuarios[index]
    raise HTTPException(status_code=400, detail="El usuario no existe")
    
# Endpoint Eliminar usuario
@app.delete('/usuario/{id}', tags=['Operaciones CRUD'])
def eliminarUsuario(id: int):
    for usr in usuarios:
        if usr["id"] == id:
            usuarios.remove(usr)  # Corrección aquí
            return {"Mensaje": "El usuario se eliminó al llavaso"}
    
    raise HTTPException(status_code=400, detail="El usuario no existe")
