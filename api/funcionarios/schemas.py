from marshmallow import Schema, validate, ValidationError
from flask import g
from .. import fields
from ..helpers import current_db_session
from ..models import Funcionario
from ..messages import Messages
from ..helpers import current_language


def exists_func_id(value: int) -> None:
    session = current_db_session()
    func = session.query(Funcionario).filter(Funcionario.id == value).first()
    if not func:
        raise ValidationError(current_language()[Messages.MISSING_BOT])
    else:
        g.func = func


class SearchSchema(Schema):

    query = fields.String(required=True, default="*")
    limit = fields.Integer(required=False, default=100, missing=100)
    skip = fields.Integer(required=False, default=0, missing=0)


class AddSchema(Schema):

    nome = fields.String(required=True)
    idade = fields.Integer(required=True)
    cargo = fields.String(required=True)


class UpdateSchema(Schema):

    func_id = fields.Integer(required=True, validate=exists_func_id)
    nome = fields.String(required=True)
    idade = fields.Integer(required=True)
    cargo = fields.String(required=True)


class DeleteSchema(Schema):

    func_id = fields.Integer(required=True, validate=exists_func_id)


class DetailSchema(Schema):
    func_id = fields.Integer(required=True, validate=exists_func_id)
