from app.models.author_model import  authors
from app import db
def listar():
    autores= authors.query.all()
    return autores
def inserir(nome):
    new_author = authors(name=nome)
    db.session.add(new_author)
    db.session.commit()

def excluir(author_id):
    author = authors.query.get(author_id)
    if author:
        db.session.delete(author)
        db.session.commit()