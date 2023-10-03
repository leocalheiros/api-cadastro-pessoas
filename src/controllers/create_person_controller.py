from src.controllers.interface.person_controller_interface import PersonInterface
from src.models.person_repository import PersonRepositoryInterface


class CreatePersonController(PersonInterface):
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
        return new_person

    def __validate(self, person: dict):
        person = name = person.get("name")
        age = person.get("age")
        neighborhood = person.get("neighborhood")
        profession = person.get("profession")

        if not (name and age and neighborhood and profession):
            raise ValueError('Parâmetros de entrada inválidos para cadastrar uma pessoa.')
