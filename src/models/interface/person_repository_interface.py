from abc import ABC, abstractmethod


class PersonRepositoryInterface(ABC):

    @abstractmethod
    def create_person(self, name, age, neighborhood, profession):
        pass

    @abstractmethod
    def find_person_by_name(self, name):
        pass

    @abstractmethod
    def delete_person_by_name(self, name):
        pass

    @abstractmethod
    def update_person(self, name, age, neighborhood, profession):
        pass

    @abstractmethod
    def list_all_people(self):
        pass

    @abstractmethod
    def person_exist(self, name):
        pass
