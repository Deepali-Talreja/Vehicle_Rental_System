from flask import jsonify , request
from services.rental_services import RentalService

def to_dict(obj) :
    return {column.name: getattr(obj, column.name) for column in obj.__table__.columns}

class RentalController :
    def __init__(self) :
        self.service = RentalService()

    def get_rental(self , rental_id):
        rental = self.service.get_rental(rental_id)
        return jsonify (to_dict(rental)) if rental else jsonify ({"error":"Rental not found"})
    
    def create_rental(self , rental_data):
        rental = self.service.create_rental(rental_data)
        return jsonify(to_dict(rental))
    
    def update_rental(self , rental_id):
        rental_data = request.json
        updated_rental = self.update_rental(rental_id , rental_data)
        return jsonify(to_dict(updated_rental)) if updated_rental else jsonify ({"error" : "rental not found"})
    
    def delete_rental(self , rental_id):
        deleted_rental = self.service.delete_rental(rental_id)
        return jsonify ({"message" : "Rental deleted"}) if deleted_rental else ({"error" : "rental not found"})
    



# RENTAL DETAILS

    def create_rentail_details(self , rental_details_data):
        rental_details = self.service.create_rental_details(rental_details_data)
    
    def get_rental_details(self , rental_id):
        rental_details = self.service.get_rental_details(rental_id)
        return jsonify(to_dict(rental_details)) if rental_details else jsonify ({"error" : "details not found"})
    
    def update_admin(self , rental_id):
        rental_details_data = request.json
        updated_rental_details= self.update_admin(rental_id , rental_details_data)
        return jsonify(to_dict(updated_rental_details)) if updated_rental_details else jsonify ({"error" : "Details not found"})
    
    def delete_admin(self , rental_id):
        deleted_rental_details = self.service.delete_admin(rental_id)
        return jsonify ({"message" : " Admin deleted "}) if deleted_rental_details else jsonify ({"error" : "Details not found"})

