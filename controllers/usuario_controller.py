#!/usr/bin/env python
"""
-----------------------------------------------------
Program    : usuario_controller.py
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
from services.usuario_service import UsuarioService
from dto.usuario_request import UsuarioRequest
from models.usuario import Usuario

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)

usuario_service = UsuarioService()

@router.get("/")
def listar_usuario():
    return usuario_service.listar_usuario()

@router.get("/{id_usuario}")
def buscar_usuario(id_usuario: int):
    return usuario_service.buscar_usuario(id_usuario)

@router.post("/")
def cadastrar_usuario(dados: UsuarioRequest):
    usuario = Usuario(
        nome = dados.nome
    )

    id_usuario = usuario_service.cadastrar_usuario(usuario)

    return {
        "id": id_usuario,
        "mensagem": "Usuario cadastrado"
    }

@router.put("/{id_usuario}")
def atualizar_usuario(dados: UsuarioRequest, id_usuario: int):
    usuario = Usuario(
        nome = dados.nome
    )
    
    usuario_service.cadastrar_usuario(usuario, id_usuario)

    return {
        "mensagem": "Usuario atualizado"
    }

@router.delete("/produtos/{id_usuario}")
def deletar_usuario(id_usuario: int):
    usuario_service.deletar_usuario(id_usuario)
    return {
        "mensagem": "Usuario removido"
    } 