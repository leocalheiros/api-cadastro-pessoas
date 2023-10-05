from src.controllers.interface.person_controller_interface import PersonInterface
from src.models.person_repository import PersonRepositoryInterface
from src.errors.types.http_not_found import HttpNotFoundError


class FindPerson(PersonInterface):
    def __init__(self, repo: PersonRepositoryInterface) -> None:
        self.__repo = repo

    def operate(self, name: str) -> str:
        self.__validate(name)
        person = self.__repo.find_person_by_name(name)
        person_dict = {
                "name": person.name,
                "age": person.age,
                "neighborhood": person.neighborhood,
                "profession": person.profession
            }
        return f"Pessoa encontrada! {person_dict}"

    def __validate(self, name) -> None:
        if not self.__repo.person_exist(name):
            raise HttpNotFoundError("Pessoa com nome não encontrada no banco de dados")
