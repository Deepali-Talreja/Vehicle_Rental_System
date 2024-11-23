from flask import jsonify , request 
from services.feedback_services import FeedbackService

def to_dict(obj):
    return {column.name : getattr(obj , column.name) for column in obj.__table__.columns}



class FeedbackController :

    def __init__(self):
        self.service = FeedbackService()
    
    def get_feedback(self , feedback_id):
        feedback = self.service.get_feedback(feedback_id)
        return jsonify (to_dict(feedback)) if feedback else jsonify ({"error" : "Feedback not found"})
    

    def create_feedback(self , feedback_data):
        feedback = self.service.create_feedback(feedback_data)
        return jsonify(to_dict(feedback))
    

    def update_feedback(self , feedback_id):
        feedback_data = request.json
        updated_feedback = self.update_feedback(feedback_id , feedback_data)
        return jsonify(to_dict(updated_feedback)) if updated_feedback else jsonify ({"error" : "Feedback not found"})
    

    def delete_feedback(self , feedback_id):
        deleted_feedback = self.service.delete_feedback(feedback_id)
        return jsonify ({"message" : "Feedback deleted"}) if deleted_feedback else ({"error" : "Feedback not found"})
    
