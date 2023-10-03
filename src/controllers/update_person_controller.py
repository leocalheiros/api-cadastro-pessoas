from src.controllers.interface.person_controller_interface import PersonInterface
from src.models.person_repository import PersonRepositoryInterface


class UpdatePerson(PersonInterface):
    def __init__(self, repo: PersonRepositoryInterface) -> None:
        self.__repo = repo

    def operate(self, person: dict) -> str:
        self.__validate(person)
        name = person["name"]
        age = person["age"]
        neighborhood = person["neighborhood"]
        profession = person["profession"]
        self.__repo.update_person(name, age, neighborhood, profession)
        return f"Cadastro da pessoa com nome '{name}' foi atualizado com sucesso"

    def __validate(self, person: dict) -> None:
        name = person.get("name")
        age = person.get("age")
        neighborhood = person.get("neighborhood")
        profession = person.get("profession")

        if not (name and age and neighborhood and profession):
            raise ValueError("Parâmetros de entrada inválidos para atualizar uma pessoa")
        if not self.__repo.person_exist(name):
            raise ValueError("Pessoa não encontrada no banco de dados")
