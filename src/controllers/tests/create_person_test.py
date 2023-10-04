from unittest.mock import MagicMock
import pytest
from src.controllers.create_person_controller import CreatePerson


class MockPersonRepository:
    def create_person(self, name, age, neighborhood, profession):
        pass

    def person_exist(self, name):
        pass


def test_create_person_success():
    repo_mock = MockPersonRepository()
    controller = CreatePerson(repo_mock)

    person_data = {
        "name": "João",
        "age": 30,
        "neighborhood": "Rua A",
        "profession": "Engenheiro"
    }

    repo_mock.create_person = MagicMock(return_value=None)

    response = controller.operate(person_data)

    assert response == "Usuário criado com sucesso!"


def test_create_person_invalid_parameters():
    repo_mock = MockPersonRepository()
    controller = CreatePerson(repo_mock)

    invalid_person_data = {
        "name": "Maria",
        "neighborhood": "Rua B",
        "profession": "Médica"
    }

    with pytest.raises(ValueError) as e:
        controller.operate(invalid_person_data)

    assert str(e.value) == "Parâmetros de entrada inválidos"


def test_create_person_user_already_exists():
    repo_mock = MockPersonRepository()
    controller = CreatePerson(repo_mock)

    existing_person_data = {
        "name": "Pedro",
        "age": 25,
        "neighborhood": "Rua C",
        "profession": "Professor"
    }

    repo_mock.person_exist = MagicMock(return_value=True)

    with pytest.raises(ValueError) as e:
        controller.operate(existing_person_data)

    assert str(e.value) == "Já existe uma pessoa com esse nome cadastrada"
