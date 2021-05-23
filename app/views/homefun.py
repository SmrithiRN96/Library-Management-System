import json
from app.app import login_manager
from app.models.usermodel import User
from app.views.booksfun import add
from flask_restful import Resource
from flask import jsonify,request,flash,render_template,redirect, url_for
from flask_login import current_user,LoginManager,login_required,login_user,logout_user

def log():
	#user login
	if request.method == 'POST':
		user = User.objects.get(usermailid=request.form["usermailid"])
		if (user.userpassword==request.form["userpassword"] and user.userrole=='admin'):
			login_user(user)
			flash('You were successfully logged in')
			return render_template('admin.html')
		elif (user.userpassword==request.form["userpassword"] and user.userrole=='user'):
			login_user(user)
			flash('You were successfully logged in')
			return render_template('user.html')
		else:
			render_template('home.html')
	return render_template('home.html')

def signup():
	#user register
	if request.method == 'POST':
		userpassword = request.form["userpassword"]
		usermailid = request.form["usermailid"]
		userrole = request.form["userrole"]
		print(request.form)
		User.objects.create(userpassword=userpassword,
			usermailid=usermailid,userrole=userrole)
		return redirect(url_for('log'))
	else:
		return render_template('signup.html')

def admin() :
	return render_template('admin.html')

def userper() :
	return render_template('user.html')

def logout():
	logout_user()
	return render_template('home.html')
