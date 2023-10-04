from unittest.mock import MagicMock
import pytest
from src.controllers.delete_person_by_name_controller import DeletePerson


class MockPersonRepository:
    def delete_person_by_name(self, name):
        pass

    def person_exist(self, name):
        pass


def test_delete_person_success():
    repo_mock = MockPersonRepository()
    controller = DeletePerson(repo_mock)

    name_to_delete = "João"

    repo_mock.delete_person_by_name = MagicMock(return_value=None)

    repo_mock.person_exist = MagicMock(return_value=True)

    response = controller.operate(name_to_delete)

    assert response == f"Pessoa com nome '{name_to_delete}' foi deletada com sucesso"


def test_delete_person_missing_name():
    repo_mock = MockPersonRepository()
    controller = DeletePerson(repo_mock)

    with pytest.raises(ValueError) as e:
        controller.operate("")

    assert str(e.value) == "Nome da pessoa não foi fornecido"


def test_delete_person_not_found():
    repo_mock = MockPersonRepository()
    controller = DeletePerson(repo_mock)

    non_existing_name = "Maria"

    repo_mock.person_exist = MagicMock(return_value=False)

    with pytest.raises(ValueError) as e:
        controller.operate(non_existing_name)

    assert str(e.value) == "Pessoa não encontrada no banco de dados"
