#!/usr/bin/env python
"""
-----------------------------------------------------
Program    : main.py
Description:
Version    : 0.1
Author     : Luca Gorayeb <lucagorayeb@gmail.com>
Date       : 13/06/2026
Lincence   : GNU/GPL v3.0
-----------------------------------------------------
Use:
-----------------------------------------------------
"""
from fastapi import FastAPI

from .controllers.produto_controller import router as produto_router
from .controllers.fornecedor_controller import router as fornecedor_router
from .controllers.usuario_controller import router as usuario_router
from .controllers.estoque_controller import router as estoque_router
from .controllers.movimentacao_controller import router as movimentacao_router
from .controllers.produto_fornecedor_controller import (
    router as produto_fornecedor_router
)

app = FastAPI(
    title = "Sistema de Estoque",
    version = "1.0"
)

@app.get("/")
def home():
    return {"mensagem":"API do Sistema de Estoque"}

app.include_router(produto_router)
app.include_router(fornecedor_router)
app.include_router(usuario_router)
app.include_router(estoque_router)
app.include_router(movimentacao_router)
app.include_router(produto_fornecedor_router)
