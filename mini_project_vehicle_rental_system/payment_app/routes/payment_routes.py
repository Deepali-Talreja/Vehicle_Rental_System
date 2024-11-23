from flask import Blueprint , request 
from controllers.payment_controllers import PaymentController


payment_route = Blueprint('payment_route' , __name__)
controller = PaymentController()

# payment routes
@payment_route.route("/payment/<int:payment_id>" , methods = ["GET"])
def get_payment(payment_id):
    return controller.get_payment(payment_id)

@payment_route.route("/payment" , methods = ["POST"])
def create_payment():
    payment_data = request.json
    return controller.create_payment(payment_data)

@payment_route.route("/payment/<int:payment_id>" , methods = ["PUT"])
def update_payment(payment_id):
    return controller.update_payment(payment_id)

@payment_route.route("/city/<int:payment_id>" , methods = ["DELETE"])
def delete_payment(payment_id):
    return controller.delete_payment(payment_id)


