#!/usr/bin/env python
"""
-----------------------------------------------------
Program    : movimentacao_controller.py
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
from services.movimentacao_service import MovimentacaoService
from api.dto.movimentacao_request import MovimentacaoRequest
from models.movimentacao import Movimentacao

router = APIRouter(
    prefix="/movimentacoes",
    tags=["Movimentacoes"]
)

movimentacao_service = MovimentacaoService()

@router.get("/")
def listar_movimentacoes():
    return movimentacao_service.listar_movimentacao()

@router.get("/{id_movimentacao}")
def buscar_movimentacoes(id_movimentacao: int):
    return movimentacao_service.buscar_movimentacao(id_movimentacao)

@router.post("/")
def cadastrar_movimentacoes(dados: MovimentacaoRequest):
    movimentacao = Movimentacao(
        produto_id = dados.produto_id,
        forncedor_id = dados.forncedor_id,
        tipo = dados.tipo,
        quantidade = dados.quantidade,
        observarcao = dados.observarcao,
        usuario_id = dados.usuario_id
    )
