from app.models.book_model import books
from app import db
def listar():
    livros = books.query.all()
    return livros
def inserir(title, author_id):
    new_book = books(title=title, author_id=author_id)
    db.session.add(new_book)
    db.session.commit()

def excluir(book_id):
    book = books.query.get(book_id)
    if book:
        db.session.delete(book)
        db.session.commit()