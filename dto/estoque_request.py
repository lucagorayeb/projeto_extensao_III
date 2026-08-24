#!/usr/bin/env python
"""
-----------------------------------------------------
Program    : estoque_request.py
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

class EstoqueRequest(BaseModel):
    prduto_id: int
    quantidade: int
    quantidade_minima: int
    localizacao: str