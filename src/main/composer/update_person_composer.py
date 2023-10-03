from src.views.update_person_view import UpdatePersonView
from src.controllers.update_person_controller import UpdatePerson
from src.models.person_repository import PersonRepository


def update_person_composer():
    repo = PersonRepository()
    controller = UpdatePerson(repo)
    view = UpdatePersonView(controller)
    return view
