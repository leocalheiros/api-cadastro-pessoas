from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interface.views_interface import ViewInterface
from src.controllers.interface.person_controller_interface import PersonInterface


class DeletePersonView(ViewInterface):
    def __init__(self, controller: PersonInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        try:
            name = http_request.body.get("name")
            response = self.__controller.operate(name)
            return HttpResponse(status_code=200, body=response)
        except Exception as exception:
            return HttpResponse(status_code=500, body={"error": str(exception)})
