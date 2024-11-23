from flask import jsonify , request 
from services.payment_services import PaymentService

def to_dict(obj):
    return {column.name : getattr(obj , column.name) for column in obj.__table__.columns}

class PaymentController :
    def __init__(self) :
        self.service = PaymentService()

    def get_payment(self , payment_id):
        payment = self.service.get_payment(payment_id)
        return jsonify (to_dict(payment)) if payment else jsonify ({"error" : "City not found"})
    

    def create_payment(self , payment_data):
        payment= self.service.create_payment(payment_data)
        return jsonify(to_dict(payment))
    

    def update_payment(self , payment_id):
        payment_data = request.json
        updated_payment = self.update_payment(payment_id , payment_data)
        return jsonify(to_dict(updated_payment)) if updated_payment else jsonify ({"error" : "Payment detail not found"})
    

    def delete_payment(self , payment_id):
        deleted_payment = self.service.delete_payment(payment_id)
        return jsonify ({"message" : "payment deleted"}) if deleted_payment else ({"error" : "Payment detail not found"})
    

