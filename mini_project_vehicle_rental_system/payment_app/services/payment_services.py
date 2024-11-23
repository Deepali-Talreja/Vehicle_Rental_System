from models.payment_models import SessionLocal , Payments

class PaymentService :
    def __init__(self) :
        self.db = SessionLocal()

    def get_payment(self , payment_id):
        return self.db.query(Payments).filter(Payments.payment_id == payment_id).first()
    
    def create_payment(self , payment_data):
        payment = Payments(**payment_data)
        self.db.add(Payments)
        self.db.commit()
        return payment
    
    def update_payment(self , payment_id , payment_data ):
        payment = self.get_car(payment_id)
        if payment :
            for key , value in payment_data.items():
                setattr(payment , key , value)
            self.db.commit()
            return payment
        
    def delete_payment(self , payment_id):
        payment = self.get_payment(payment_id)
        if payment :
            self.db.delete(payment)
            self.db.commit()
            return payment
        