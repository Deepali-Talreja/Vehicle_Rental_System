from models.customer_models import SessionLocal , Customers

class CustomerService :
    def __init__(self):
        self.db = SessionLocal()

    # CUSTOMER 
    def create_customer(self , customer_data):
        customer = Customers(**customer_data)
        self.db.add(customer)
        self.db.commit()
        return customer
        
    def get_customer(self , customer_id):
        return self.db.query(Customers).filter(Customers.customer_id == customer_id).first()
        

    def update_customer(self , customer_id , customer_data):
        customer = self.get_customer(customer_id)
        if customer:
            for key , value in customer_data.items():
                setattr(customer , key , value)
            self.db.commit()
            return customer
            
        
    def delete_customer(self , customer_id):
        customer = self.get_customer(customer_id)
        if Customers :
            self.db.delete(customer)
            self.db.commit()
            return customer
            

