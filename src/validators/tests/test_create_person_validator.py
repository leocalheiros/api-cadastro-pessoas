import pytest
from src.validators.all_fields_person_validator import all_fields_validator
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
        all_fields_validator(request)
