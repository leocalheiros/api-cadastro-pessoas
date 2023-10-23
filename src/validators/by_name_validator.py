from cerberus import Validator
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError


def by_name_validator(request: any):

    body_validator = Validator({
        'name': {'type': 'string', 'required': True, 'empty': False},
    })

    response = body_validator.validate({"name": request})

    if response is False:
        raise HttpUnprocessableEntityError(body_validator.errors)
