# Biblioteka_2_0
Module 13.4
task:Biblioteka 2.0

My home library app

The requirements.txt file contains all the modules that are needed for the application to work properly.

Initially, you can test the application with the test database: library.db that is attached.

After activate installed virtual environment, you need to type 'flask run' into your command line being in the folder where the 'library.py' is.

Type http://localhost:5000/books/ in your browser to view the list of books in the database.

To check selected list you can use links located on the website:
Go to the list of authors
Go to the list of books
Go to the list of borrowings

On http://localhost:5000/books/ you can also add a new book but remember that you have to add new author first if he/she's not yet on the list to choose. To add new author go to http://localhost:5000/authors/.
By click on the existing title you can see details of this book, you can change the data or delete it from database.

On http://localhost:5000/authors/ you can see the list of authors. You can add new author as well.
By click on the author name you can see all of his/her books in the library. You can delete the author if needed.

On http://localhost:5000/borrowing/ you can see the list of book borrowings.
You can type selected book id and change its status to returned.
You can borrow selected book by adding information about the title, when and to whom it was borrowed.
