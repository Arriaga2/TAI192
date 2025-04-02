from fastapi import FastAPI
from DB.conexion import engine, Base
from routers.usuario import routerUsuario
from routers.auth import routerAuth

app = FastAPI(
    title='My FastAPI 192', 
    description='API de Jelipe',
    version='1.0.1',
)

# Endpoint home
@app.get('/', tags=['Hola Chavito'])
def home():
    return {'hello': 'world FastAPI'}

app.include_router(routerUsuario)
app.include_router(routerAuth)

Base.metadata.create_all(bind=engine)


