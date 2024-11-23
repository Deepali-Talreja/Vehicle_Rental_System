from flask import Blueprint , request 
from controllers.rental_controllers import RentalController


rental_route = Blueprint('rental_route' , __name__)
controller = RentalController()

# rental routes
@rental_route.route("/rental/<int:rental_id>" , methods = ["GET"])
def get_rental(rental_id):
    return controller.get_rental(rental_id)

@rental_route.route("/rental" , methods = ["POST"])
def create_rental():
    rental_data = request.json
    return controller.create_rental(rental_data)

@rental_route.route("/rental/<int:rental_id>" , methods = ["PUT"])
def update_rental(rental_id):
    return controller.update_rental(rental_id)

@rental_route.route("/rental/<int:rental_id>" , methods = ["DELETE"])
def delete_rental(rental_id):
    return controller.delete_rental(rental_id)


# details routes
@rental_route.route("/rental_details/<int:rental_id>" , methods = ["GET"])
def get_rental_details(rental_id):
    return controller.get_rental_details(rental_id)

@rental_route.route("/rental_details" , methods = ["POST"])
def  create_rental_details(rental_id):
    return controller.create_rental_details(rental_id)

@rental_route.route("/rental_details/<int:rental_id>" , methods = ["PUT"])
def update_rental_details(rental_id):
    return controller.update_rental_details(rental_id)

@rental_route.route("/rental_details/<int:rental_id>" , methods = ["DELETE"])
def delete_rental_details(rental_id):
    return controller.delete_rental_details(rental_id)

