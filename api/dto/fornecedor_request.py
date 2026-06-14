#!/usr/bin/env python
"""
-----------------------------------------------------
Program    : fornecedor_request.py
Description:
Version    : 0.1
Author     : Luca Gorayeb <lucagorayeb@gmail.com>
Date       : 14/06/2026
Lincence   : GNU/GPL v3.0
-----------------------------------------------------
Use:
-----------------------------------------------------
"""
from pydantic import BaseModel

class FornecedorRequest(BaseModel):
    nome: str
    cpf_cnpj: str
    email: str
    telefone: str 
    endereco: str
    cidade: str
    estado: str