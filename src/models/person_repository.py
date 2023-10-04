from src.models.interface.person_repository_interface import PersonRepositoryInterface
from src.models.person_model import PersonModel
from src.main.config.database import db


class PersonRepository(PersonRepositoryInterface):
    def create_person(self, name, age, neighborhood, profession):
        person = PersonModel(name=name, age=age, neighborhood=neighborhood, profession=profession)
        db.session.add(person)
        db.session.commit()

    def find_person_by_name(self, name):
        person = PersonModel.query.filter_by(name=name).first()
        return person

    def delete_person_by_name(self, name):
        person = self.find_person_by_name(name)
        db.session.delete(person)
        db.session.commit()

    def update_person(self, name, age, neighborhood, profession):
        person = self.find_person_by_name(name)
        person.age = age
        person.neighborhood = neighborhood
        person.profession = profession
        db.session.commit()

    def list_all_people(self):
        all_people = PersonModel.query.all()
        return all_people

    def person_exist(self, name):
        person = self.find_person_by_name(name)
        return bool(person)
