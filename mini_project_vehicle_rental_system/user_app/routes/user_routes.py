from flask import Blueprint , request 
from controllers.user_controllers import UserController


user_route = Blueprint('user_route' , __name__)
controller = UserController()

# user routes
@user_route.route("/user/<int:user_id>" , methods = ["GET"])
def get_user(user_id):
    return controller.get_user(user_id)

@user_route.route("/user" , methods = ["POST"])
def create_user():
    user_data = request.json
    return controller.create_user(user_data)

@user_route.route("/user/<int:user_id>" , methods = ["PUT"])
def update_user(user_id):
    return controller.update_user(user_id)

@user_route.route("/user/<int:user_id>" , methods = ["DELETE"])
def delete_user(user_id):
    return controller.delete_user(user_id)


# admin routes
@user_route.route("/admin/<int:admin_id>" , methods = ["GET"])
def get_admin(admin_id):
    return controller.get_admin(admin_id)

@user_route.route("/admin" , methods = ["POST"])
def  create_admin(admin_id):
    return controller.create_admin(admin_id)

@user_route.route("/admin/<int:admin_id>" , methods = ["PUT"])
def update_admin(admin_id):
    return controller.update_admin(admin_id)

@user_route.route("/admin/<int:admin_id>" , methods = ["DELETE"])
def delete_admin(admin_id):
    return controller.delete_admin(admin_id)
