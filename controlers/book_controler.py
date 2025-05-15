from app import db
from app import app
from flask import Flask, render_template, request, redirect, url_for

from app.models.book_model import books
from app.services import book_service

#with app.app_context():
 #   db.create_all()  # Create database tables for data models

@app.route('/books', methods=['GET'])
def home():

    livros= book_service.listar()
    return render_template('books.html', livros=livros)

@app.route('/add', methods=['POST'])
def add_book():
    title = request.form.get('title')
    author_id= request.form.get('author_id')

    book_service.inserir(title,author_id)
    return redirect(url_for('home'))

@app.route('/delete/<int:book_id>', methods=['POST'])
def delete_book(book_id):
    book_service.excluir(book_id)
    return redirect(url_for('home'))



