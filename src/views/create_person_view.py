from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interface.views_interface import ViewInterface
from src.controllers.interface.person_controller_interface import PersonInterface
from src.validators.all_fields_person_validator import all_fields_validator
from src.errors.error_handler import handle_errors


class CreatePersonView(ViewInterface):
    def __init__(self, controller: PersonInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        try:
            person_data = http_request.body
            all_fields_validator(person_data)
            response = self.__controller.operate(person_data)
            return HttpResponse(status_code=200, body={"response": response})
        except Exception as exception:
            return handle_errors(exception)
