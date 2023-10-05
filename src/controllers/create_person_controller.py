from src.controllers.interface.person_controller_interface import PersonInterface
from src.models.person_repository import PersonRepositoryInterface
from src.errors.types.http_not_found import HttpNotFoundError


class CreatePerson(PersonInterface):
    def __init__(self, repo: PersonRepositoryInterface) -> None:
        self.__repo = repo

    def operate(self, person: dict) -> str:
        self.__validate(person)
        new_person = self.__repo.create_person(
            person["name"],
            person["age"],
            person["neighborhood"],
            person["profession"]
        )
        return "Usuário criado com sucesso!"

    def __validate(self, person: dict) -> None:
        name = person.get("name")

        if self.__repo.person_exist(name):
            raise HttpNotFoundError("Pessoa com nome não encontrada no banco de dados")
