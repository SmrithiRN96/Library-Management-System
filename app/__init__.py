#routers
from app.app import api, app, login_manager
from app.models.usermodel import User
from app.views.homefun import log,signup,admin,userper,logout
from app.views.booksfun import add,delete,update,view,userview,useradd

login_manager.init_app(app)
@login_manager.user_loader
def load_user(user):
    """current user details"""
    return User.objects.get(id=user)
#for login
app.add_url_rule("/", view_func=log, methods=["GET","POST"])
#for signup
app.add_url_rule("/signup", view_func=signup, methods=["GET","POST"])
#for admin page
app.add_url_rule("/admin", view_func=admin, methods=["GET","POST"])
#for admin adding books
app.add_url_rule("/add", view_func=add, methods=["GET","POST"])
#for admin updating books
app.add_url_rule("/update", view_func=update, methods=["GET","POST"])
#for admin deleting books
app.add_url_rule("/delete", view_func=delete, methods=["GET","POST"])
#for admin viewing books
app.add_url_rule("/view",view_func=view,methods=["GET","POST"])
#for user page
app.add_url_rule("/userper", view_func=userper, methods=["GET","POST"])
#for user viewing books
app.add_url_rule("/userview", view_func=userview, methods=["GET","POST"])
#for user adding books
app.add_url_rule("/useradd", view_func=useradd, methods=["GET","POST"])
#for logout
app.add_url_rule("/logout", view_func=logout, methods=["GET","POST"])




