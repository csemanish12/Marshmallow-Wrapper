from orm import db


class User(db.Model):
    __table__name = 'users'
    id = db.Column(db.String, primary_key=True, auto_increment=True)
    name = db.Column(db.String())

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all(cls):
        return User.query.all()