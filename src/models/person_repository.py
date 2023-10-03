from src.models.interface.person_repository_interface import PersonRepositoryInterface
from src.models.person_model import PersonModel


class PersonRepository(PersonRepositoryInterface):
    def __init__(self, db):
        self.db = db

    def create_person(self, name, age, neighborhood, profession):
        person = PersonModel(name=name, age=age, neighborhood=neighborhood, profession=profession)
        self.db.session.add(person)
        self.db.session.commit()

    def find_person_by_name(self, name):
        person = PersonModel.query.filter_by(name=name).first()
        return person

    def delete_person_by_name(self, name):
        person = self.find_person_by_name(name)
        self.db.session.delete(person)
        self.db.session.commit()

    def update_person(self, name, age, neighborhood, profession):
        person = self.find_person_by_name(name)
        person.age = age
        person.neighborhood = neighborhood
        person.profession = profession
        self.db.session.commit()

    def list_all_people(self):
        all_people = PersonModel.query.all()
        return all_people

    def person_exist(self, name):
        person = self.find_person_by_name(name)
        return bool(person)
