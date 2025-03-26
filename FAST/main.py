from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import Optional, List
from modelsPydantic import modeloUsuario, modeloAuth
from genToken import createToken
from middlewares import BearerJWT
from DB.conexion import Session, engine, Base
from models.modelsDB import User

app = FastAPI(
    title='My FastAPI 192', 
    description='API de Jelipe',
    version='1.0.1',
)

Base.metadata.create_all(bind=engine)

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

# Endpoint Autenticacion
@app.post('/auth',tags=['Autentificación'])
def login(autorizacion:modeloAuth):
    if autorizacion.correo == 'jelipe@example.com' and autorizacion.passw == '123456789':
        token:str = createToken(autorizacion.model_dump())
        print(token)
        return JSONResponse(content=token)
    else:
        return{"Aviso": "Usuario no autorizado"}

# Endpoint CONSULTA TODOS
@app.get('/todoUsuarios', tags=['Operaciones CRUD'])
def leerUsuarios():
    db= Session()
    try:
        consulta=db.query(User).all()
        return JSONResponse(content= jsonable_encoder(consulta))
    
    except Exception as e:
        return JSONResponse(status_code=500,
                            content={"message": "Error al agregar usuario",
                                     "Excepcion": str(e)})
    finally:
        db.close()



# Endpoint buscar por id
@app.get('/usuario/{id}', tags=['Operaciones CRUD'])
def buscarUno(id:int):
    db= Session()
    try:
        consultauno=db.query(User).filter(User.id == id).first()

        if not consultauno:
            return JSONResponse(status_code=404,content= {"Mensaje":"Usuario no encontrado"})
        
        return JSONResponse(content= jsonable_encoder(consultauno))
    
    except Exception as e:
        return JSONResponse(status_code=500,
                            content={"message": "Error al agregar usuario",
                                     "Excepcion": str(e)})
    finally:
        db.close()


# Endpoint Agregar nuevos
@app.post('/usuario/',  response_model= modeloUsuario ,tags=['Operaciones CRUD'])
def agregarUsuario(usuario:modeloUsuario):
    db= Session()
    try:
        db.add( User( **usuario.model_dump()))
        db.commit()
        return JSONResponse(status_code=201,
                            content={"message": "Usuario agregado con exito",
                                      "usuario":usuario.model_dump() })
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500,
                            content={"message": "Error al agregar usuario",
                                     "Excepcion": str(e)})
    finally:
        db.close()
    


# Endpoint Actualizar Usuarios
@app.put('/usuario/{id}',  response_model= modeloUsuario ,tags=['Operaciones CRUD'])
def actualizarUsuario(id:int, usuarioActualizado:modeloUsuario):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[index] = usuarioActualizado.model_dump()
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
