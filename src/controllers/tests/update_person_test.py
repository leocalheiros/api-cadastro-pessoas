from unittest.mock import MagicMock
import pytest
from src.controllers.update_person_controller import UpdatePerson


class MockPersonRepository:
    def update_person(self, name, age, neighborhood, profession):
        pass

    def person_exist(self, name):
        pass


def test_update_person_success():
    repo_mock = MockPersonRepository()
    controller = UpdatePerson(repo_mock)

    person_data = {
        "name": "João",
        "age": 30,
        "neighborhood": "Centro",
        "profession": "Engenheiro"
    }

    repo_mock.person_exist = MagicMock(return_value=True)

    response = controller.operate(person_data)

    expected_response = f"Cadastro da pessoa com nome 'João' foi atualizado com sucesso"
    assert response == expected_response


def test_update_person_missing_data():
    repo_mock = MockPersonRepository()
    controller = UpdatePerson(repo_mock)

    incomplete_person_data = {
        "name": "João",
        "age": 30,
        "neighborhood": "Centro",
    }

    with pytest.raises(ValueError) as e:
        controller.operate(incomplete_person_data)

    assert str(e.value) == "Parâmetros de entrada inválidos para atualizar uma pessoa"


def test_update_person_not_found():
    repo_mock = MockPersonRepository()
    controller = UpdatePerson(repo_mock)

    person_data = {
        "name": "Maria",
        "age": 25,
        "neighborhood": "Centro",
        "profession": "Engenheira"
    }

    repo_mock.person_exist = MagicMock(return_value=False)

    with pytest.raises(ValueError) as e:
        controller.operate(person_data)

    assert str(e.value) == "Pessoa não encontrada no banco de dados"
