from . import db


# In the context of an ORM, a model is typically a Python class with attributes that
# match the columns of a corresponding database table.

# Required Tables define as Models
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    # a __repr__() method to give models a readable string representation that can be used for debugging and testing purposes.
    def __repr__(self):
        return f"<Role {self.name}>"

class User(db.Model):
    __tablename__= 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return f"<User {self.username}>"