from flask import Blueprint , request 
from controllers.feedback_controllers import FeedbackController


feedback_route = Blueprint('feedback_route' , __name__)
controller = FeedbackController()

# feedback routes
@feedback_route.route("/feedback/<int:feedback_id>" , methods = ["GET"])
def get_feedback(feedback_id):
    return controller.get_feedback(feedback_id)

@feedback_route.route("/feedback" , methods = ["POST"])
def create_feedback():
    feedback_data = request.json
    return controller.create_feedback(feedback_data)

@feedback_route.route("/feedback/<int:feedback_id>" , methods = ["PUT"])
def update_feedback(feedback_id):
    return controller.update_feedback(feedback_id)

@feedback_route.route("/feedback/<int:feedback_id>" , methods = ["DELETE"])
def delete_feedback(feedback_id):
    return controller.delete_feedback(feedback_id)


