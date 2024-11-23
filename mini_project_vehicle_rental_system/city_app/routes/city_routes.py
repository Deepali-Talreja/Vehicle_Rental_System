from flask import Blueprint , request 
from controllers.city_controllers import CityController


city_route = Blueprint('city_route' , __name__)
controller = CityController()

# city routes
@city_route.route("/city/<int:city_id>" , methods = ["GET"])
def get_city(city_id):
    return controller.get_city(city_id)

@city_route.route("/city" , methods = ["POST"])
def create_city():
    city_data = request.json
    return controller.create_city(city_data)

@city_route.route("/city/<int:city_id>" , methods = ["PUT"])
def update_city(city_id):
    return controller.update_city(city_id)

@city_route.route("/city/<int:city_id>" , methods = ["DELETE"])
def delete_city(city_id):
    return controller.delete_city(city_id)


