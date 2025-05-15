from app import db


class authors(db.Model):
    __tablename__ = "authors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    books = db.relationship('books', backref='authors')
    def __repr__(self):
        return '<Author {}>'.format(self.nome)

