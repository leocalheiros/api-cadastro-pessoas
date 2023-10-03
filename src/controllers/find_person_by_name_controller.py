from src.controllers.interface.person_controller_interface import PersonInterface
from src.models.person_repository import PersonRepositoryInterface


class FindPerson(PersonInterface):
    def __init__(self, repo: PersonRepositoryInterface) -> None:
        self.__repo = repo

    def operate(self, name: str) -> str:
        self.__validate(name)
        person = self.__repo.find_person_by_name(name)
        return person

    def __validate(self, name) -> None:
        if not name:
            raise ValueError("Nome da pessoa não foi fornecido")
        if not self.__repo.person_exist(name):
            raise ValueError("Pessoa com nome não encontrada no banco de dados")
