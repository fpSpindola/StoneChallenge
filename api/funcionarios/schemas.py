from marshmallow import Schema, validate, ValidationError
from flask import g
from .. import fields
from ..helpers import current_db_session
from ..models import Funcionario
from ..messages import Messages
from ..helpers import current_language


def exists_func_id(value: int) -> None:
    session = current_db_session()
    bot = session.query(Funcionario).filter(Funcionario.id == value).first()
    if not bot:
        raise ValidationError(current_language()[Messages.MISSING_BOT])
    else:
        g.bot = bot


class SearchSchema(Schema):

    query = fields.String(required=True, default="*")
    limit = fields.Integer(required=False, default=100, missing=100)
    skip = fields.Integer(required=False, default=0, missing=0)


class AddSchema(Schema):

    name = fields.String(required=True, validate=[validate.Length(min=3, max=30)])
    config = fields.Dict(required=True)
    internal_config = fields.Dict(required=False, default={}, missing={})
    # type_id = fields.Integer(required=True, validate=[exists_type_id])
    sleep_time = fields.Integer(required=False, default=60, missing=60)
    enabled = fields.Boolean(required=True, default=True)


class UpdateSchema(Schema):

    # bot_id = fields.Integer(required=True, validate=exists_bot_id)
    name = fields.String(required=False, validate=[validate.Length(min=3, max=30)])
    config = fields.Dict(required=True)
    internal_config = fields.Dict(required=False, default={}, missing={})
    sleep_time = fields.Integer(required=False, default=60, missing=60)
    enabled = fields.Boolean(required=False, default=True)


class DeleteSchema(Schema):

    func_id = fields.Integer(required=True, validate=exists_func_id)


class DetailSchema(Schema):
    func_id = fields.Integer(required=True, validate=exists_func_id)
