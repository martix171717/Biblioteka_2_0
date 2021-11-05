from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import DataRequired
from app.models import Book, Author


class BooksForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    year = IntegerField('Publication Year')
    author = SelectField('Choose an author')

    @classmethod
    def new(cls):
        form = cls()
        form.author.choices = [x.name for x in Author.query.all()]
        return form


class AuthorForm(FlaskForm):
    name = StringField('Author', validators=[DataRequired()])


class BorrowingForm(FlaskForm):
    title = SelectField('Choose a title')
    date = StringField('Date of borrowing, yyyy-mm-dd', validators=[DataRequired()])
    where = StringField('Who borrowed', validators=[DataRequired()])

    @classmethod
    def new(cls):
        form = cls()
        form.title.choices = [x.title for x in Book.query.all()]
        return form


class DeleteForm(FlaskForm):
    id = IntegerField('Id', validators=[DataRequired()])