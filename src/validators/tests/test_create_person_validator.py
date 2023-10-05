import pytest
from src.validators.create_person_validator import create_person_validator
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError


class MockRequest:
    def __init__(self) -> None:
        self.json = None


def test_create_person_validator_fail():
    request = MockRequest()
    request.json = {
        "name": 123,
        "age": "abc",
        "neighborhood": "rua formosa",
        "profession": "sotware engineer"
    }

    with pytest.raises(HttpUnprocessableEntityError):
        create_person_validator(request)
