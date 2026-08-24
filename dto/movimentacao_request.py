#!/usr/bin/env python
"""
-----------------------------------------------------
Program    : movimentacao_request.py
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

class MovimentacaoRequest(BaseModel):
    produto_id: int
    forncedor_id: int
    tipo: str
    quantidade: int 
    observarcao: str
    usuario_id: int