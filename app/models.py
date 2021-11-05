from app import db

author_book = db.Table('author_book',
    db.Column('author_id', db.Integer, db.ForeignKey('author.id'), primary_key=True),
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key=True)
)

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True)
    
    def __str__(self):
        return f"Author {self.name}"
      
    def __repr__(self):
        return f"{self.name}"

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String(100), index=True)
    year = db.Column(db.Numeric(4, 0))
    author = db.relationship('Author', secondary=author_book, backref=db.backref('books', lazy='dynamic'))
    borrowed = db.relationship('Borrowing', backref='book')

    def __repr__(self):
        if self.borrowed:
            return f"{self.title}, {self.author}, {self.year}, {self.borrowed[-1]}"  
        else:
            return f"{self.title}, {self.author}, {self.year}, the book is at home library"
    def __str__(self):
        if self.borrowed:
            return f"{self.title}, {self.author}, {self.year}, {self.borrowed[-1]}"  
        else:
            return f"{self.title}, {self.author}, {self.year}, the book is at home library"  


class Borrowing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    borrowed = db.Column(db.Boolean())
    borrow_date = db.Column(db.String(10))
    where = db.Column(db.String(50))
    id_book = db.Column(db.String, db.ForeignKey('book.title'))

    def __repr__(self):
        if self.borrowed is True:
            return f"borrowed to {self.where}, {self.borrow_date}"
        else:
            return f"the book is at home library"
         
    def __str__(self):
        if self.borrowed is True:
            return f"borrowed to {self.where}, {self.borrow_date}"
        else:
            return f"the book is at home library"
