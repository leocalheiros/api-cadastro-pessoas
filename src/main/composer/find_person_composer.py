from src.views.find_person_view import FindPersonView
from src.controllers.find_person_by_name_controller import FindPerson
from src.models.person_repository import PersonRepository


def find_person_composer():
    repo = PersonRepository()
    controller = FindPerson(repo)
    view = FindPersonView(controller)
    return view
