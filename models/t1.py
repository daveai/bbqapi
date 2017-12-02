from db import db
from sqlalchemy import exc
class t1(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	PIC = db.Column(db.String(120), nullable=False)
	def __repr__(self):
		return '<User %r>' % self.username
	def insert(obj):
		db.session.add(obj)
		try:
			db.session.commit()
		except exc.SQLAlchemyError as e:
			print(e.orig)
			return False
			raise
		else:
			pass
		finally:
			pass
		
