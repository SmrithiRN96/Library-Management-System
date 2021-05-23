from app.app import db
from app.models.usermodel import User

class UserBook(db.Document) :
	bname = db.StringField(required=True)
	bauthor = db.StringField(required=True)
	bookid = db.StringField(required=True)
	bookuser = db.ReferenceField(User)