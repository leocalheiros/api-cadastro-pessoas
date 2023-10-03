from src.views.delete_person_view import DeletePersonView
from src.controllers.delete_person_by_name_controller import DeletePerson
from src.models.person_repository import PersonRepository


def delete_person_composer():
    repo = PersonRepository()
    controller = DeletePerson(repo)
    view = DeletePersonView(controller)
    return view
