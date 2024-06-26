# main.py

import requests
from fastapi import FastAPI, HTTPException

app = FastAPI()

# Endpoint para obter carros da API do Django
@app.get("/cars/")
def get_cars():
    try:
        response = requests.get("http://localhost:8000/api/cars/")
        response.raise_for_status()
        
        if response.headers.get("content-type") == "application/json":
            return response.json()
        else:
            raise HTTPException(status_code=500, detail="Resposta da API do Django não está no formato JSON")
        
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Erro ao acessar API do Django: {str(e)}")
