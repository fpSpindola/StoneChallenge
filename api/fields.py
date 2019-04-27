from marshmallow import fields, ValidationError

error_messages = {
    "required": "Este campo é obrigatório.",
    "type": "Valor inválido.",  # used by Unmarshaller
    "null": "Este campo não pode ser nulo.",
    "validator_failed": "Valor inválido.",
}


class String(fields.String):
    default_error_messages = error_messages


class Integer(fields.Integer):
    default_error_messages = error_messages


class Boolean(fields.Boolean):
    default_error_messages = error_messages


class List(fields.List):
    default_error_messages = error_messages


class DateTime(fields.DateTime):
    default_error_messages = error_messages


class Email(fields.Email):
    default_error_messages = error_messages


class Nested(fields.Nested):
    default_error_messages = error_messages


class Dict(fields.Dict):
    default_error_messages = error_messages
