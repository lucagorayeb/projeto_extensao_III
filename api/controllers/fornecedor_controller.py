#!/usr/bin/env python
"""
-----------------------------------------------------
Program    : fornecedor_controller.py
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
from services.fornecedor_service import FornecedorService
from api.dto.fornecedor_request import FornecedorRequest
from models.fornecedor import Fornecedor

router = APIRouter(
    prefix="/fornecedores",
    tags=["Fornecedores"]
)

fornecedor_service = FornecedorService()

@router.get("/")
def listar_fornecedores():
    return fornecedor_service.listar_fornecedor()

@router.get("/{id_fornecedor}")
def buscar_fornecedor(id_fornecedor: int):
    return fornecedor_service.buscar_fornecedor(id_fornecedor)

@router.post("/")
def cadastrar_fornecedor(dados: FornecedorRequest):
    fornecedor = Fornecedor(
        nome = dados.nome,
        cpf_cnpj = dados.cpf_cnpj,
        email = dados.email,
        telefone = dados.telefone, 
        endereco = dados.endereco,
        cidade = dados.cidade,
        estado = dados.estado
    )

    id_fornecedor = fornecedor_service.cadastrar_fornecedor(fornecedor)

    return {
        "id": id_fornecedor,
        "mensagem": "Fornecedor cadastrado"
    }

@router.put("/{id_fornecedor}")
def cadastrar_fornecedor(dados: FornecedorRequest, id_fornecedor: int):
    fornecedor = Fornecedor(
        nome = dados.nome,
        cpf_cnpj = dados.cpf_cnpj,
        email = dados.email,
        telefone = dados.telefone, 
        endereco = dados.endereco,
        cidade = dados.cidade,
        estado = dados.estado
    )

    fornecedor_service.atualizar_fornecedor(fornecedor, id_fornecedor)

    return {
        "mensagem": "Fornecedor atualizado"
    }

@router.delete("/{id_fornecedor}")
def deletar_produtos(id_fornecedor: int):
    fornecedor_service.deletar_fornecedor(id_fornecedor)

    return {
        "mensagem": "Fornecedor removido"
    }