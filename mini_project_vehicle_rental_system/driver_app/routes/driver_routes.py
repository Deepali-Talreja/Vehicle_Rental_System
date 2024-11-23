from flask import Blueprint , request 
from controllers.driver_controllers import DriverController


driver_route = Blueprint('driver_route' , __name__)
controller = DriverController()

# driver routes
@driver_route.route("/driver/<int:driver_id>" , methods = ["GET"])
def get_user(user_id):
    return controller.get_user(user_id)

@driver_route.route("/driver" , methods = ["POST"])
def create_driver():
    driver_data = request.json
    return controller.create_driver(driver_data)

@driver_route.route("/driver/<int:driver_id>" , methods = ["PUT"])
def update_driver(driver_id):
    return controller.update_driver(driver_id)

@driver_route.route("/driver/<int:driver_id>" , methods = ["DELETE"])
def delete_driver(driver_id):
    return controller.delete_driver(driver_id)


# # driver rates routes
# @driver_route.route("/driver_rates/<int:driver_id>/<date:effective_from>" , methods = ["GET"])
# def get_driver_details(driver_id , effective_from):
#     return controller.get_driver_details(driver_id , effective_from)

# @driver_route.route("/driver_rates" , methods = ["POST"])
# def  create_driver_details(driver_id , effective_from):
#     return controller.create_driver_details(driver_id , effective_from)

# @driver_route.route("/driver_rates/<int:driver_id>/<date:effective_from>" , methods = ["PUT"])
# def update_driver_details(driver_id , effective_from):
#     return controller.update_driver_details(driver_id , effective_from)

# @driver_route.route("/driver_rates/<int:driver_id>/<date:effective_from>" , methods = ["DELETE"])
# def delete_driver_details(driver_id , effective_from):
#     return controller.delete_driver_details(driver_id , effective_from)
