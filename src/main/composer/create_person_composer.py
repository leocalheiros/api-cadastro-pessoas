from src.views.create_person_view import CreatePersonView
from src.controllers.create_person_controller import CreatePerson
from src.models.person_repository import PersonRepository


def create_person_composer():
    repo = PersonRepository()
    controller = CreatePerson(repo)
    view = CreatePersonView(controller)
    return view
