from app.app import db

class User(db.Document):
	usermailid = db.StringField(required=True,unique=True)
	userrole = db.StringField(required=True)
	userpassword = db.StringField(required=True)
	

	def is_authenticated(self):
		return True

	def get_id(self):
		return str(self.id)

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_role(self):
		return self.role

	def check_role(self, roles):
		return self.role in roles
