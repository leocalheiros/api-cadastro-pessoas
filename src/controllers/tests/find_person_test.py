from unittest.mock import MagicMock
import pytest
from src.controllers.find_person_by_name_controller import FindPerson


class MockPersonRepository:
    def find_person_by_name(self, name):
        pass

    def person_exist(self, name):
        pass


class MockPerson:
    def __init__(self, name, age, neighborhood, profession):
        self.name = name
        self.age = age
        self.neighborhood = neighborhood
        self.profession = profession


def test_find_person_success():
    repo_mock = MockPersonRepository()
    controller = FindPerson(repo_mock)

    name_to_find = "João"

    mock_person = MockPerson(name="João", age=30, neighborhood="Centro", profession="Engenheiro")
    repo_mock.find_person_by_name = MagicMock(return_value=mock_person)

    repo_mock.person_exist = MagicMock(return_value=True)

    response = controller.operate(name_to_find)

    expected_response = f"Pessoa encontrada! {{'name': 'João', 'age': 30, 'neighborhood': 'Centro', 'profession': 'Engenheiro'}}"
    assert response == expected_response


def test_find_person_missing_name():
    repo_mock = MockPersonRepository()
    controller = FindPerson(repo_mock)

    with pytest.raises(ValueError) as e:
        controller.operate("")

    assert str(e.value) == "Nome da pessoa não foi fornecido"


def test_find_person_not_found():
    repo_mock = MockPersonRepository()
    controller = FindPerson(repo_mock)

    non_existing_name = "Maria"

    repo_mock.person_exist = MagicMock(return_value=False)

    with pytest.raises(ValueError) as e:
        controller.operate(non_existing_name)

    assert str(e.value) == "Pessoa com nome não encontrada no banco de dados"
