from src.main.config.database import db


class PersonModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    neighborhood = db.Column(db.String(255), nullable=False)
    profession = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<Pessoa: {self.id}, {self.name}, {self.age}, {self.neighborhood}, {self.profession}>'
