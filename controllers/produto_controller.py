#!/usr/bin/env python
"""
-----------------------------------------------------
Program    : produto_controller.py
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
from services.produto_service import ProdutoService
from api.dto.produto_request import ProdutoRequest
from models.produto import Produto

router = APIRouter(
    prefix="/produtos",
    tags=["Produtos"]
)

produto_service = ProdutoService()

@router.get("/")
def listar_produtos():
    return produto_service.listar_produto()

@router.get("/{id_produto}")
def buscar_produto(id_produto: int):
    return produto_service.buscar_produto(id_produto)

@router.post("/")
def cadastrar_produto(dados: ProdutoRequest):
    produto = Produto(
        nome = dados.nome,
        descricao = dados.descricao,
        codigo_barra = dados.codigo_barra,
        preco_custo = dados.preco_custo,
        vendivel = dados.vendivel,
        preco_venda = dados.preco_venda,
        categoria = dados.categoria
    )

    id_produto = produto_service.cadastrar_produto(produto)

    return {
        "id": id_produto,
        "mensagem": "Produto cadastrado"
    }

@router.put("/{id_produto}")
def atualizar_produto(dados: ProdutoRequest, id_produto: int):
    produto = Produto(
        nome = dados.nome,
        descricao = dados.descricao,
        codigo_barra = dados.codigo_barra,
        preco_custo = dados.preco_custo,
        vendivel = dados.vendivel,
        preco_venda = dados.preco_venda,
        categoria = dados.categoria
    )

    produto_service.atualizar_produto(produto, id_produto)

    return {
        "mensagem": "Produto atualizado"
    }

@router.delete("/{id_produto}")
def deletar_produto(id_produto: int):
    produto_service.deletar_produto(id_produto)
    return{
        "mensagem": "Produto deletado"
    }

