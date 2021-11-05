from app import app, db
from app.models import Author, Book, Borrowing


@app.shell_context_processor
def make_shell_context():
    return {
       "db": db,
       "Book": Book,
       "Author": Author,
       "Borrowing": Borrowing}


if __name__ == "__main__":
    app.run(debug=True)
