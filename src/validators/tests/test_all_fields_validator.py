from src.validators.all_fields_person_validator import all_fields_validator
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError
import pytest


def test_valid_request():
    valid_request = {
        'name': 'João',
        'age': 30,
        'neighborhood': 'Centro',
        'profession': 'Engenheiro'
    }

    all_fields_validator(valid_request)


def test_invalid_request():
    invalid_request = {
        'name': 'Maria',
        'neighborhood': 'Bairro'
    }

    with pytest.raises(HttpUnprocessableEntityError):
        all_fields_validator(invalid_request)
