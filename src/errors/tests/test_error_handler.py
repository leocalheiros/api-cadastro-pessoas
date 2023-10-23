from unittest.mock import MagicMock
import pytest
from src.errors.error_handler import handle_errors
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError
from src.errors.types.http_not_found import HttpNotFoundError
from src.errors.types.http_bad_request import HttpBadRequestError


def test_handle_errors_http_not_found():
    error = HttpNotFoundError("Resource not found")
    response = handle_errors(error)
    assert response.status_code == 404
    assert response.body == {
        "errors": [{
            "title": "NotFound",
            "detail": "Resource not found"
        }]
    }


def test_handle_errors_http_bad_request():
    error = HttpBadRequestError("Bad request")
    response = handle_errors(error)
    assert response.status_code == 400
    assert response.body == {
        "errors": [{
            "title": "BadRequest",
            "detail": "Bad request"
        }]
    }


def test_handle_errors_http_unprocessable_entity():
    error = HttpUnprocessableEntityError("Unprocessable entity")
    response = handle_errors(error)
    assert response.status_code == 422
    assert response.body == {
        "errors": [{
            "title": "UnprocessableEntity",
            "detail": "Unprocessable entity"
        }]
    }


def test_handle_errors_generic_error():
    error = Exception("Generic error")
    response = handle_errors(error)
    assert response.status_code == 500
    assert response.body == {
        "errors": [{
            "title": "Server Error",
            "detail": "Generic error"
        }]
    }
