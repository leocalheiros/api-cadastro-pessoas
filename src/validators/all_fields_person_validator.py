from cerberus import Validator
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError


def all_fields_validator(request: any):

    body_validator = Validator({
        'name': {'type': 'string', 'required': True, 'empty': False},
        'age': {'type': 'integer', 'required': True, 'empty': False},
        'neighborhood': {'type': 'string', 'required': True, 'empty': False},
        'profession': {'type': 'string', 'required': True, 'empty': False},
    })

    response = body_validator.validate(request)

    if response is False:
        raise HttpUnprocessableEntityError(body_validator.errors)
