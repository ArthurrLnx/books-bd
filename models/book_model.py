from app import db

class books(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))

    def __repr__(self):
        return '<Book {}>'.format(self.title)


