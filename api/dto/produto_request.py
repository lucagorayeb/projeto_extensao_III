#!/usr/bin/env python
"""
-----------------------------------------------------
Program    : produto_request.py
Description:
Version    : 0.1
Author     : Luca Gorayeb <lucagorayeb@gmail.com>
Date       : 13/06/2026
Lincence   : GNU/GPL v3.0
-----------------------------------------------------
Use:
-----------------------------------------------------
"""
from pydantic import BaseModel

class ProdutoRequest(BaseModel):
    nome: str
    descricao: str
    codigo_barra: str
    preco_custo: float 
    vendivel: bool
    preco_venda: float
    categoria: str

