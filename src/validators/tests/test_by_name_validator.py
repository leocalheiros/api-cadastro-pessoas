import pytest
from src.validators.by_name_validator import by_name_validator
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError


def test_valid_request():
    valid_name = 'João'

    by_name_validator(valid_name)


def test_invalid_request():
    invalid_name = ''

    with pytest.raises(HttpUnprocessableEntityError):
        by_name_validator(invalid_name)
