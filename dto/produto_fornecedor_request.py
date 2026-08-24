#!/usr/bin/env python
"""
-----------------------------------------------------
Program    : produto_fornecedor_request.py
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

class ProdutoFornecedorRequest(BaseModel):
    produto_id: int
    fornecedor_id: int