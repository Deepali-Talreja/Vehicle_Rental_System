from flask import Blueprint , request 
from controllers.car_controllers import CarController


car_route = Blueprint('car_route' , __name__)
controller = CarController()

# user routes
@car_route.route("/car/<int:car_id>" , methods = ["GET"])
def get_car(car_id):
    return controller.get_car(car_id)

@car_route.route("/car" , methods = ["POST"])
def create_car():
    car_data = request.json
    return controller.create_car(car_data)

@car_route.route("/car/<int:car_id>" , methods = ["PUT"])
def update_car(car_id):
    return controller.update_car(car_id)

@car_route.route("/car/<int:car_id>" , methods = ["DELETE"])
def delete_car(car_id):
    return controller.delete_car(car_id)


