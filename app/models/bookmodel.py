from app.app import db

class Books(db.Document) :
	bname = db.StringField(required=True)
	bauthor = db.StringField(required=True)
	bookid = db.StringField(required=True)
