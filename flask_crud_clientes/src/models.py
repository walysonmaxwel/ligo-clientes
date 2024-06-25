from . import db

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    client_id = db.Column(db.String(100), nullable=False, unique=True)
    client_secret = db.Column(db.String(100), nullable=False, unique=True)
    inclusion_date = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'email': self.email,
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'inclusion_date': self.inclusion_date
        }
