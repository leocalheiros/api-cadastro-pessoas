from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interface.views_interface import ViewInterface
from src.controllers.interface.person_controller_interface import PersonInterface
from src.validators.by_name_validator import by_name_validator
from src.errors.error_handler import handle_errors


class FindPersonView(ViewInterface):
    def __init__(self, controller: PersonInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        try:
            name = http_request.body.get("name")
            by_name_validator(name)
            response = self.__controller.operate(name)
            return HttpResponse(status_code=200, body={"message": response})
        except Exception as exception:
            return handle_errors(exception)
        