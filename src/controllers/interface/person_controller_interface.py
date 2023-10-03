from abc import ABC, abstractmethod


class PersonInterface(ABC):

    @abstractmethod
    def operate(self, person: dict) -> str:
        pass
