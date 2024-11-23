from models.feedback_models import SessionLocal , Feedbacks

class FeedbackService :
    def __init__(self) :
        self.db = SessionLocal()

    def get_feedback(self , feedback_id):
        return self.db.query(Feedbacks).filter(Feedbacks.feedback_id == feedback_id).first()
    
    def create_feedback(self , feedback_data):
        feedback = Feedbacks(**feedback_data)
        self.db.add(Feedbacks)
        self.db.commit()
        return feedback
    
    def update_feedback(self , feedback_id , feedback_data ):
        feedback = self.get_feedback(feedback_id)
        if feedback :
            for key , value in feedback_data.items():
                setattr(feedback , key , value)
            self.db.commit()
            return feedback
        
    def delete_feedback(self , feedback_id):
        feedback = self.get_feedback(feedback_id)
        if feedback :
            self.db.delete(feedback)
            self.db.commit()
            return feedback
        