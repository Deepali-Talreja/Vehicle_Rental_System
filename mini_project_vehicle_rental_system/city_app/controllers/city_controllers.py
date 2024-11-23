from flask import jsonify , request 
from services.city_services import CityService

def to_dict(obj):
    return {column.name : getattr(obj , column.name) for column in obj.__table__.columns}



class CityController :

    def __init__(self):
        self.service = CityService()
    
    def get_city(self , city_id):
        city = self.service.get_city(city_id)
        return jsonify (to_dict(city)) if city else jsonify ({"error" : "City not found"})
    

    def create_city(self , city_data):
        city = self.service.create_city(city_data)
        return jsonify(to_dict(city))
    

    def update_city(self , city_id):
        city_data = request.json
        updated_city = self.update_city(city_id , city_data)
        return jsonify(to_dict(updated_city)) if updated_city else jsonify ({"error" : "City not found"})
    

    def delete_city(self , city_id):
        deleted_city = self.service.delete_city(city_id)
        return jsonify ({"message" : "City deleted"}) if deleted_city else ({"error" : "City not found"})
    
