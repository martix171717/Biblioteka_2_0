from flask import Flask, jsonify, abort, make_response, request, render_template, redirect, url_for 
from app import db, app
from app.models import Book, Author, Borrowing
from app.forms import BooksForm, AuthorForm, DeleteForm, BorrowingForm
from datetime import date

@app.route("/", methods=["GET"])
def main():
    return render_template("index.html")

#wyświetla wszystkie książki w bazie, pozwala na dodanie nowej książki
@app.route("/books/", methods=["GET", "POST"])
def books_list():
    form = BooksForm.new()
    books_all = Book.query.all()
    if request.method == "POST":
        if form.validate_on_submit():
            book1 = Book(title=form.title.data, year=form.year.data)
            db.session.add(book1)
            db.session.commit()
            author1 = Author.query.filter_by(name=form.author.data).first()
            author1.books.append(book1)
            db.session.commit()
            books_all = Book.query.all()
            return redirect(url_for("books_list"))
    return render_template("books.html", books=books_all, form=form)


#wyświetla wszystkich autorów w bazie, pozwala utworzyć nową pozycję autora
@app.route("/authors/", methods=["GET", "POST"])
def authors_list():
    form = AuthorForm()
    authors = Author.query.all()
    if request.method == "POST":
        if form.validate_on_submit():
            author1 = Author(name=form.name.data)
            db.session.add(author1)
            db.session.commit()
            authors = Author.query.all()
            return redirect(url_for("authors_list"))
    return render_template("authors.html", authors=authors, form=form)

#wyświetla szczegóły o wypozyczeniach, pozwala na wypożyczenie i zwrot wybranej ksiązki
@app.route("/borrowing/", methods=["GET", "POST"])
def borrowing_list():
    form = BorrowingForm.new()
    form2 = DeleteForm()
    borrowing = Borrowing.query.all()
    books = Book.query.all()
    if request.method == "POST":
        if form.validate_on_submit():
            book1 = Book.query.filter_by(title=form.title.data).first()
            borrow = Borrowing(borrowed=True, borrow_date=form.date.data, where=form.where.data, book=book1) 
            db.session.add(borrow)
            db.session.commit()
            borrowing = Borrowing.query.all()
            return redirect(url_for("borrowing_list"))
        if form2.validate_on_submit():
            borrow = Borrowing.query.filter_by(id=form2.id.data).first()
            borrow.borrowed = False
            borrow.where = f"Returned by {borrow.where}"
            borrow.borrow_date= date.today()
            db.session.commit()
            return redirect(url_for("borrowing_list"))
    return render_template("borrowing.html", borrowing=borrowing, form=form, books=books, form2=form2)


#wyświetla konkretny rekord z bazy danych, umożliwia zmianę danych lub usunięcie książki  
@app.route("/books/<int:book_id>", methods=["GET", "POST"])
def get_book(book_id):
    form = BooksForm().new()
    book = Book.query.get(book_id)
    if request.method == "POST":
        book = Book.query.get(book_id)
        book.title = form.title.data
        book.year = form.year.data
        db.session.commit()
        author1 = Author.query.filter_by(name=form.author.data).first()
        author1.books.append(book)
        db.session.commit()
        return redirect('/books/<int:book_id>')
    return render_template("book.html", book=book, form=form, book_id=book_id)

#wyświetla konkretnego autora z bazy danych, umożliwia usunięcie autora
@app.route("/authors/<int:author_id>", methods=["GET", "POST"])
def get_authors_books(author_id):
    form = DeleteForm()
    author = Author.query.get(author_id)
    books = author.books
    if not author:
        abort(404)
    if request.method == "POST":
        book = Book.query.filter_by(id=form.id.data).first()
        author.books.remove(book)
        db.session.commit()
        return redirect(url_for("get_authors_books"))
    return render_template("author_books.html", author=author.name, books=books, author_id=author_id, form=form)  # noqa: E501


# usuwa rekord książki o danym id z bazy danych
@app.route("/books/delete/<int:book_id>", methods=['GET'])
def delete_book(book_id):
    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()
    return render_template("books.html", books=Book.query.all(), form=BooksForm()) 


# usuwa rekord autora z bazy danych
@app.route("/authors/delete/<int:author_id>", methods=['GET'])
def delete_author(author_id):
    author = Author.query.get(author_id)
    db.session.delete(author)
    db.session.commit()
    return render_template("authors.html", authors=Author.query.all(), form=AuthorForm()) 


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found', 'status_code': 404}), 404) 


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request', 'status_code': 400}), 400)  
