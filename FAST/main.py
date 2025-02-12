from fastapi import FastAPI, HTTPException
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

# Endpoint CONSULTA TODOS
@app.get('/todoUsuarios', tags=['Operaciones CRUD'])
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
            usuarios.remove(usr)
            return {"Mensaje": "El usuario ha sido eliminado"}
        return {"Mensaje": "El usuario no existe"}
