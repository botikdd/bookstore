from app import db

from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer

class Database:
	__instance = None

	@staticmethod 
	def getInstance():
		if Database.__instance == None:
			Database()
		return Database.__instance

	def __init__(self):
		if Database.__instance != None:
			raise Exception("This class is a singleton!")
		else:
			Database.__instance = self

	def get_book(self, book_id):
		return db.session.query.filter((Book.id == book_id)).first()

	def get_books(self):
		return db.session.query(Book).all()

	def add_book(self, title, author):
		book = Book(title = title, author = author)

		print(book)

		db.session.add(book)
		db.session.commit()

class Book(db.Model):
	__tablename__ = 'book'

	id = Column(Integer, primary_key=True)
	title = Column(String(), nullable=False)
	author = Column(String(), nullable=False)

	def __init__(self, title, author):
		self.title = title
		self.author = author

	def __repr__(self):
		return '<id: {}; title: {}; author: {}>'.format(self.id, self.title, self.author)