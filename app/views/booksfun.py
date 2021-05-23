import uuid
from flask import jsonify,request,render_template,redirect, url_for
from flask_login import current_user
from app.models.usermodel import User
from app.models.bookmodel import Books
from app.models.userbookmodel import UserBook

def add() :
	if request.method == 'GET' :
		additems = Books.objects.all()
		return render_template('add.html',additems=additems)
	if request.method == 'POST' :
		bname = request.form['bname']
		bauthor = request.form['bauthor']
		uniqueuid = uuid.uuid4().hex
		bookid = uniqueuid
		#Books.objects.create(bname=bname,
		#	bauthor=bauthor,bookid=uniqueuid)
		#user =  User.objects.get(id=current_user.id)
		#additems = Books.objects(adduser=current_user.id)
		additems = Books.objects.all()
		books = Books(bname=bname,bauthor=bauthor,bookid=bookid).save()
		return render_template('add.html',additems=additems)
	return render_template('add.html')

def update() :
	if request.method == 'GET' :
		updatebooks = Books.objects.all()
		return render_template('update.html',updatebooks=updatebooks)
	if request.method == 'POST' :
		updatebooks = Books.objects.all()
		bname = request.form['bname']
		bauthor = request.form['bauthor']
		bookid = request.form['bookid']
		books = Books.objects.get_or_404(bookid=bookid)
		books.update(bname=bname,bauthor=bauthor)
		return render_template('update.html',updatebooks=updatebooks)
	return render_template('update.html')

def delete() :
	if request.method == 'GET' :
		deletebooks = Books.objects.all()
		return render_template('delete.html',deletebooks=deletebooks)
	if request.method == 'POST' :
		deletebooks = Books.objects.all()
		bookid = request.form['bookid']
		books = Books.objects.get_or_404(bookid=bookid)
		books.delete()
		return render_template('delete.html',deletebooks=deletebooks)
	return render_template('delete.html')

def view() :
	if request.method == 'GET' :
		books = Books.objects.all()
		return render_template('view.html',books=books)
	

def userview() :
	if request.method == 'GET' :
		books = Books.objects.all()
		return render_template('userview.html',books=books)

def useradd() :
	if request.method == 'GET' :
		books = Books.objects.all()
		bookitems = UserBook.objects(bookuser=current_user.id)
		return render_template('useradd.html',bookitems=bookitems,books=books)
	if request.method == 'POST' :
		bookid = request.form['bid']
		books = Books.objects.get(bookid=bookid)
		user = User.objects.get(id=current_user.id)
		bookitems = UserBook.objects(bookuser=current_user.id)
		userbook = UserBook(bname=books.bname,bauthor=books.bauthor,bookid=books.bookid,bookuser=current_user.id).save()
		return render_template('useradd.html',bookitems=bookitems)
