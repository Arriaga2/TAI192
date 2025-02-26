from pydantic import BaseModel, Field

#modelo de validaciones 
class modeloUsuario(BaseModel):
    id:int = Field(...,gt=0,description="Id unico y solo numeros positivos")
    nombre:str = Field(...,min_lenght=3, max_length=85,description="Solo letras: min 3 max 85")
    edad:int = Field(...,ge=0,le=120,description="Mayor de 0 y menor de 121")
    correo: str = Field(..., pattern="^[\w\.-]+@[\w\.-]+\.\w+$", examples=["mario@example.com"])


                                            
                                                                 
                

