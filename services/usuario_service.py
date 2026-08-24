
"""
-----------------------------------------------------
Program    : usuario_service.py
Description:
Version    : 0.1
Author     : Luca Gorayeb <lucagorayeb@gmail.com>
Date       : 13/06/2026
Licence   : GNU/GPL v3.0
-----------------------------------------------------
Use:
-----------------------------------------------------
"""
from repositories.usuario_repository import UsuarioRepository, CAMPOS_VALIDOS
from models.usuario import Usuario 


class UsuarioService:
    def __init__(self):
        self._usuario_repository = UsuarioRepository('estoque.sqlite')
    
    def cadastrar_usuario(self, usuario: Usuario):
        return self._usuario_repository.salvar(usuario)
    
    def atualizar_usuario(self, usuario: Usuario, id_usuario: int):
        return self._usuario_repository.atualizar(usuario, id_usuario)
    
    def deletar_usuario(self, id_usuario: int):
        return self._usuario_repository.deletar(id_usuario)

    def buscar_usuario(self, id_usuario: int):
        return self._usuario_repository.buscar_por_id(
            list(CAMPOS_VALIDOS), id_usuario
        )
    
    def listar_usuario(self):
        return self._usuario_repository.listar(
            list(CAMPOS_VALIDOS)
        )