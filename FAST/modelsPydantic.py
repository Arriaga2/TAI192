from pydantic import BaseModel, Field, EmailStr

#modelo de validaciones 
class modeloUsuario(BaseModel):
    name:str = Field(...,min_lenght=3, max_length=85,description="Solo letras: min 3 max 85")
    age:int = Field(...,ge=0,le=120,description="Mayor de 0 y menor de 121")
    email: EmailStr = Field(..., description="Debe ser un correo electrónico válido")

class modeloAuth(BaseModel):
    correo: EmailStr = Field(..., description="Debe ser un correo electrónico válido", example="example@gmail.com")
    passw: str =Field(..., min_length=8, strip_whitespace=True, description="contraseña minimo 8 caracteres")
                                            
                                                                 
                

