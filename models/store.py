from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    location = db.Column(db.String(255), nullable=True)

    def __init__(self, name, location):
        self.name = name
        self.location = location

    def __repr__(self):
        return f"<Store(id={self.id}, name={self.name})>"
