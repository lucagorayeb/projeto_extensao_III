#!/usr/bin/env python
"""
-----------------------------------------------------
Program    : produto_fornecedor_controller.py
Description:
Version    : 0.1
Author     : Luca Gorayeb <lucagorayeb@gmail.com>
Date       : 14/06/2026
Lincence   : GNU/GPL v3.0
-----------------------------------------------------
Use:
-----------------------------------------------------
"""
from fastapi import APIRouter
from services.produto_fornecedor_service import ProdutoFornecedorService
from dto.produto_fornecedor_request import ProdutoFornecedorRequest
from models.produto_fornecedor import ProdutoFornecedor

router = APIRouter(
    prefix="/produto-fornecedor",
    tags=["ProdutosFornecedor"]
)

produto_fornecedor_service = ProdutoFornecedorService()

@router.get("/")
def listar_produto_fornecedor():
    return produto_fornecedor_service.listar_produto_fornecedor()

@router.get("/{id_produto_fornecedor}")
def buscar_produto_fornecedor(id_produto_fornecedor: int):
    return produto_fornecedor_service.buscar_produto_fornecedor(id_produto_fornecedor)

@router.post("/")
def cadastrar_produto_fornecedor(dados: ProdutoFornecedorRequest):
    produto_fornecedor = ProdutoFornecedor(
        produto_id = dados.produto_id,
        fornecedor_id = dados.fornecedor_id
    )

    produto_fornecedor_id = produto_fornecedor_service.cadastrar_produto_fornecedor(produto_fornecedor)

    return {
        "id": produto_fornecedor_id,
        "mensagem": "Produto-Fornecedor cadastrado"
    }

@router.delete("/{id_produto_fornecedor}")
def deletar_produto_fornecedor(id_produto_fornecedor: int):
    produto_fornecedor_service.deletar_produto_fornecedor(id_produto_fornecedor)

    return {
        "mensagem": "Produto-Fornecedor removido"
    }