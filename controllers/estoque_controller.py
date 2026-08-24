#!/usr/bin/env python
"""
-----------------------------------------------------
Program    : estoque_controller.py
Description:
Version    : 0.1
Author     : Luca Gorayeb <lucagorayeb@gmail.com>
Date       : 13/06/2026
Lincence   : GNU/GPL v3.0
-----------------------------------------------------
Use:
-----------------------------------------------------
"""
from fastapi import APIRouter
from services.estoque_service import EstoqueService
from dto.estoque_request import EstoqueRequest
from models.estoque import Estoque

router = APIRouter(
    prefix="/estoque",
    tags=["Estoque"]
)

estoque_service = EstoqueService()

@router.get("/")
def listar_estoque():
    return estoque_service.listar_estoque()

@router.get("/{id_estoque}")
def buscar_estoque(id_estoque: int):
    return estoque_service.buscar_estoque(id_estoque)

@router.post("/{id_estoque}/entrada")
def entrada_estoque(dados: EstoqueRequest):
    estoque = Estoque(
        produto_id = dados.produto_id,
        quantidade = dados.quantidade,
        quantidade_minima = dados.quantidade_minima,
        localizacao = dados.localizacao
    )

    estoque_id = estoque_service.entrada_estoque(estoque)

    return {
        "id": estoque_id,
        "mensagem": "Entrada no estoque registrada"
    }

@router.post("/{id_estoque}/entrada")
def retirada_estoque(dados: EstoqueRequest):
    estoque = Estoque(
        produto_id = dados.produto_id,
        quantidade = dados.quantidade,
        quantidade_minima = dados.quantidade_minima,
        localizacao = dados.localizacao
    )

    estoque_id = estoque_service.saida_estoque(estoque)

    return {
        "id": estoque_id,
        "mensagem": "Saida no estoque registrada"
    }