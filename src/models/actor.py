import uuid

from src import db


class Actor(db.Model):
    __tablename__ = "actors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    birthday = db.Column(db.Date)
    is_active = db.Column(db.Boolean, default=False)
    uuid = db.Column(db.String(36), unique=True)

    def __init__(self, name, birthday, is_active):
        self.name = name
        self.birthday = birthday
        self.is_active = is_active
        self.uuid = str(uuid.uuid4())

    def __repr__(self):
        return f"Actor ({self.uuid}, {self.name}, {self.birthday}, {self.is_active})"

    def to_dict(self):
        return {
            "name": self.name,
            "birthday": self.birthday.strftime("%Y-%m-%d"),
            "is_active": self.is_active,
            "uuid": self.uuid,
        }
