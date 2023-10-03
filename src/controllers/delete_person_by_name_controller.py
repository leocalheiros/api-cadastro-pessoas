from src.controllers.interface.person_controller_interface import PersonInterface
from src.models.person_repository import PersonRepositoryInterface


class DeletePerson(PersonInterface):
    def __init__(self, repo: PersonRepositoryInterface) -> None:
        self.__repo = repo

    def operate(self, name: str) -> str:
        self.__validate(name)
        self.__repo.delete_person_by_name(name)
        return f"Pessoa com nome '{name}' foi deletada com sucesso"

    def __validate(self, name: str) -> None:
        if not name:
            raise ValueError("Nome da pessoa não foi fornecido")
        if not self.__repo.person_exist(name):
            raise ValueError("Pessoa não encontrada no banco de dados")
