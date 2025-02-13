from fastapi import FastAPI, HTTPException
from typing import Optional


app = FastAPI(
    title='API Repaso S-192',
    description='Creado Por Jelipe',
    version='1.0.1'
)

# Endpoint home
@app.get('/', tags=['Calando el rollo'])
def home():
    return {'hello': 'world FastAPI'}

