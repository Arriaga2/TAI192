from pydantic import BaseModel, Field

# Modelo de validaciones 
class modeloConductor(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=85, description="Solo letras: min 3 max 85")
    TipoLicencia: int = Field(...,gt=0,description="Id unico y solo numeros positivos")
    NoLicencia: str = Field(..., min_length=1, max_length=12, description="Solo max 12 caracteres")
