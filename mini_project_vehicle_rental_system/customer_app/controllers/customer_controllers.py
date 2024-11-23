from flask import jsonify , request
from services.customer_services import CustomerService

def to_dict(obj):
    return {column.name : getattr(obj , column.name) for column in obj.__table__.columns}


class CustomerController :
    def __init__(self):
        self.service = CustomerService()
    
    # CUSTOMER 

    def create_customer(self , customer_data):
        customer =self.service.create_customer(customer_data)
        return jsonify(to_dict(customer))
    

    def get_customer(self , customer_id):
        customer = self.service.get_customer(customer_id)
        return jsonify(to_dict(customer)) if customer else jsonify ({"error" : "Customer not found"})
    

    def update_customer(self , customer_id):
        customer_data = request.json
        updated_customer = self.update_customer(customer_id , customer_data)
        return jsonify(to_dict(updated_customer)) if updated_customer else jsonify ({"error" : "Customer not found"})
    
    def delete_customer(self , customer_id) :
        deleted_customer = self.service.delete_customer(customer_id)
        return jsonify({"message" : "Customer deleted"}) if deleted_customer else jsonify ({"error" : "Customer not found"})
    


