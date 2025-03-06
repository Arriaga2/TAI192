import jwt
from jwt import ExpiredSignatureError, InvalidTokenError
from fastapi import HTTPException

def createToken(data: dict):
    token = jwt.encode(payload=data, key="secretkey", algorithm="HS256")
    return token

def validateToken(token: str):
    try:
        data = jwt.decode(token, key="secretkey", algorithms=["HS256"])
        return data
    except ExpiredSignatureError:
        raise HTTPException(status_code=403, detail="Token expirado")
    except InvalidTokenError:
        raise HTTPException(status_code=403, detail="Token no autorizado")
