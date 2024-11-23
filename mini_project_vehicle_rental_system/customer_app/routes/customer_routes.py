from flask import Blueprint , request 
from controllers.customer_controllers import CustomerController


customer_route = Blueprint('customer_route' , __name__)
controller = CustomerController()

# user routes
@customer_route.route("/customer/<int:customer_id>" , methods = ["GET"])
def get_customer(customer_id):
    return controller.get_customer(customer_id)

@customer_route.route("/customer" , methods = ["POST"])
def create_customer():
    customer_data = request.json
    return controller.create_customer(customer_data)

@customer_route.route("/customer/<int:customer_id>" , methods = ["PUT"])
def update_customer(customer_id):
    return controller.update_customer(customer_id)

@customer_route.route("/customer/<int:customer_id>" , methods = ["DELETE"])
def delete_customer(customer_id):
    return controller.delete_customer(customer_id)


